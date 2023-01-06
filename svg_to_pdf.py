from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import fitz
import os
import re


def atoi(text):
    return int(text) if text.isdigit() else text

# Function alist.sort(key=natural_keys) sorts in human order
# More info: http://nedbatchelder.com/blog/200712/human_sorting.html
def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# !PDF destination folder must exist. If not - prior to the render add os.mkdir(pdf_folder)
svg_folder = "SVG SOURCE FOLDER NAME"
pdf_folder = "PDF DESTINATION FOLDER NAME"

# Geting the list of files and sorting it in human order (1,2,3,..10,11,12) 
files = os.listdir(folder)
files.sort(key=natural_keys)

# Making pdf's file by file and saving them
for svg in files:
  drawing = svg2rlg(svg_folder + svg)
  renderPDF.drawToFile(drawing, pdf_folder + svg.replace('.svg','.pdf'))
