from docx import Document
from docx.enum.style import WD_STYLE_TYPE



def create_doc():
    document = Document()

    document.add_heading('Pkm trial', 0)
    document.save('demo.docx')
    print(f'Document created')
    return None
    