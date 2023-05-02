from backend import fillDoc
from frontend import getInfo
from pywebio.output import put_file, put_html
from pywebio.session import hold

title = "<h1 style=\"text-align:center\">O'zbekiston Respublikasi fuqorosining xorijga chiqish  biometrik pasportini rasmiylashtirish uchun ANKETA</h1>"
put_html(title)

userInfo = getInfo()
filename = fillDoc(userInfo)

text = "<h3>Anketa tayyor. Yuklab olish uchun quyidagi bog'lamani bosing.</h3>"
put_html(text)

with open(filename, 'rb') as fayl:
    anketa = fayl.read()
    put_file(filename, content=anketa)
    hold()