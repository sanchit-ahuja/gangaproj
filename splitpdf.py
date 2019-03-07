from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("/home/sanchit/Desktop/gangaproj/PDFiles/CERN.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)