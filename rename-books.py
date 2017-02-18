from pyPdf import PdfFileWriter, PdfFileReader
import os

directory = './books/'

for fileName in os.listdir(directory):
    try:
        if fileName.lower()[-3:] != "pdf":
            print('not a pdf');
            continue
        input1 = PdfFileReader(file(directory + fileName, "rb"))

    # print the title of document1.pdf
        print('##pass ' + fileName + ' ' + input1.getDocumentInfo().title)
    except Exception as e:
        print('##fail ' + fileName + ' ' + str(e))
