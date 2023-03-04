import PyPDF2


class Parser:
    def __init__(self, filename):
        paper = open(filename, 'rb')
        self.paper = PyPDF2.PdfFileReader(paper)

    def get_text(self):
        pdf_text = []
        for i in range(0, self.paper.numPages):
            page = self.paper.getPage(i)
            text = page.extract_text()
            pdf_text.append(text)

        return pdf_text



