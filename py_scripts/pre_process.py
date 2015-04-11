'''
@author:    Gaurav Sood
@title:     Preprocess text documents
@date:      4/10/2015

Steps
    1) Import BeautifulSoup, nltk (download stopwords etc. -- a separate step), urlopen
    2) Run
       python pre_process.py

'''

import re
import os
import string
import unicodedata

from urllib import urlopen
from BeautifulSoup import BeautifulSoup

import sys
sys.path.append("C:\Users\gaurav\Dropbox\python\packages")
print sys.path
from BeautifulSoup import BeautifulSoup

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import EnglishStemmer

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Get data
# open url
url  = urlopen('http://www.weeklystandard.com/print/blogs/transcript-netanyahus-address-congress_873668.html').read()
# get the soup
soup = BeautifulSoup(url)
# contents of p
text= soup.findAll(text=True)
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

visible_text = filter(visible, text)
print visible_text

# List to string
type(visible_text)
text = "".join(visible_text)
print text[200:700]

# Encode to ascii
type(text)
text = text.encode('ascii', 'ignore')

# Take out \n
text = re.sub("\n", "", text)
print text[len(text)-1000:len(text)]

# lower case
text = text.lower()
print text[len(text)-1000:len(text)]

# remove punctuation
text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
print text[len(text)-1000:len(text)]

# stemming
st = PorterStemmer()
words = wordpunct_tokenize(text)
words = [st.stem(w) for w in words]
text = ' '.join(words)
print text[len(text)-1000:len(text)]

