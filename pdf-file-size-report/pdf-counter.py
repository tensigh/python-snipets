# This lets me get all the PDFs
# in a directory
#
# Then it gets their number of pages
# then it saves report to desktop

from pyPdf import PdfFileReader
import os

pdflist = []
sourcePath = "/path/to/PDFs"

for root, dirs, files in os.walk(sourcePath):
     for thing in files:
       if thing[-4:].upper() == ".PDF":
        pdffile = os.path.join(root, thing)
        pdflist.append(pdffile)

with open("/path/to/reports/pdf-list.csv","wb") as targetFile:
 with open("/path/to/reports/pdf-errors.csv","wb") as errFile:
  for item in pdflist:
    try:
     pdfsize = PdfFileReader(file(item, "rb"))
     numPages = pdfsize.getNumPages()
     targetFile.write(item + "|" + str(numPages) + "\n") # using Pipe instead of comma
    except Exception as error:
     errFile.write(str(error) + "|" + item + "\n") # using Pipe instead of comma; comma is sometimes in filename