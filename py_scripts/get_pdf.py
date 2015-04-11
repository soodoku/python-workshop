'''
@author:	Gaurav Sood
@title:		Get text of pdfs 
@date:		4/10/2015

Steps:
	1) install pyPdf
	2) Set the path etc.
	3) Run the script
		python get_pdf.py
'''

import os, pyPdf

pdf = pyPdf.PdfFileReader(file('pdf_file', "rb"))
content = pdf.getPage(0).extractText()
print content

content 	= content.encode("ascii", "xmlcharrefreplace")
title 		= ' '.join(content.split(' ')[1:]).partition('Brand:')[0]
race 		= content.split(' ')[0]  
parent 		= content.partition('Parent:')[2].partition('Aired:')[0]
date 		= content.partition('Aired:')[2].partition('Creative Id:')[0].strip()
creative_id = content.partition('Creative Id:')[2].partition('[')[0]

print "------------"
print "title: " + title
print "race: " + race
print "parent: " + parent
print "date: " + date
print "creative_id: " + creative_id


# Multiple Files
path = 'path_to_dir_of_pdf_files'
dirList=os.listdir(path)
for fname in dirList:
    pdf = pyPdf.PdfFileReader(file(path+fname, "rb"))
    content = pdf.getPage(0).extractText().encode("ascii", "xmlcharrefreplace")
    print content
    print "----------------------------"