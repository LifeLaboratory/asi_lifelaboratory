# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader
import file

output = PdfFileWriter()
input1 = PdfFileReader(file("document1.pdf", "rb"))
watermark = PdfFileReader(file("watermark.pdf", "rb"))

page4.mergePage(watermark.getPage(0))

# finally, write "output" to document-output.pdf
outputStream = file("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()