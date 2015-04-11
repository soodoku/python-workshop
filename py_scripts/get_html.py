'''
@author:	Gaurav Sood
@title:		Get text of html
@date:		4/10/2015

Steps:
	1) install BeautifulSoup, urllib (these days urllib2)
	2) Run the script
		python get_html.py

'''

# import libs
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
import urllib2, urlparse
import re

# open url
url  = urlopen('http://bit.ly/1D7wKcH').read()
# get the soup
soup = BeautifulSoup(url)
# contents of p
text = soup.p.contents
print text

# find stuff in the soup
soup.findAll(text=re.compile("VALENTINE"))
soup.findAll('a', {'name' : '1.1.28'})
soup.findAll('blockquote')

# Using it to sequentially going through links
soupy = BeautifulSoup(urllib2.urlopen('http://search.espncricinfo.com/ci/content/match/search.html?search=odi;all=1;page=1'))
for new_host in soupy.findAll('a', {'class' : 'srchPlyrNmTxt'}):
	print new_host['href']
	try:
		new_host = new_host['href']
	except:
		continue
	odiurl = 'http://www.espncricinfo.com' + new_host
	soup = BeautifulSoup(urllib2.urlopen(odiurl).read())
	temp = soup.findAll(text=re.compile("ODI no. "))
	print temp
