"""
PDF Watermark Project

This Python program is designed to place a watermark on each page of a given pdf.

Libraries:
    PyPDF2

Input:
    A PDF file that is the watermark.
    A PDF file that the watermark will be placed on.

Output:
    1 PDF file.

Execute:
    Press the run button once the desired PDF and Watermark are placed in the
    project folder. Make sure to chance the names inside the code to the names
    of the pdf and watermark. Also make sure to change the output name to the
    desired name.

Author: James Mitchell
    This is a part of the Computer Python Developer in 2020: Zero to Mastery
    course on Udemy.com provided by Andrei Neagoie.

"""

import PyPDF2

pdf = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(pdf.getNumPages()):
    page = pdf.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)

