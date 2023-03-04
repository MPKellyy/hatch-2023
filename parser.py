import PyPDF2


def get_text_from_pdf(filename):
    file = open(filename, 'rb')
    paper = PyPDF2.PdfReader(file)
    pdf_text = []
    num_pages = len(paper.pages)
    for i in range(0, num_pages):
        page = paper.pages[i]
        text = page.extract_text()
        pdf_text.append(text)

    file.close()
    return pdf_text


