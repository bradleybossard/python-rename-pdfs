from PyPDF2 import PdfFileWriter, PdfFileReader
import os

from pathlib import Path

#dir = '/home/bradleybossard/src/cheatsheets/reading-lists'
# directory = './books/'
dir = '/Users/bradleybossard/Downloads/Takeout/Google Play Books'
pattern = '*.pdf'

for filename in Path(dir).glob(pattern):
    if filename.is_dir():
        continue
    with open(filename, 'rb') as file:
        input1 = PdfFileReader(file)
        try:
            # print the title of document1.pdf
            print('##pass ' + str(filename) + '       ' + str(input1.getDocumentInfo().title))
        except Exception as e:
            print('##fail ' + str(filename) + ' ' + str(e))
