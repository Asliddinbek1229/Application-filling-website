from docxtpl import DocxTemplate

def fillDoc(info, file="anketa.docx"):
        anketa = DocxTemplate('anketa.docx')
        anketa.render(info)
        filename = f"{info['familiya']}_anketa.docx"
        anketa.save(filename)
        return filename

