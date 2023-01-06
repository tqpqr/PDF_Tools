import fitz
import os
import re


# Function alist.sort(key=natural_keys) sorts in human order
# More info: http://nedbatchelder.com/blog/200712/human_sorting.html
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

folder = "FOLDER WITH PDFs/pdf/"
output_file_path = folder + "OUTPUT_PDF.pdf"

files = os.listdir(folder)
files.sort(key=natural_keys)

doc = fitz.open()

for pdf in files:
    infile = fitz.open(folder+pdf)
    lastPage = len(infile) - 1
    doc.insert_pdf(infile, from_page=lastPage, to_page=lastPage)
    infile.close()
doc.save(output_file_path, deflate=True, garbage=3)
