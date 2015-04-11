'''

@author:	Gaurav Sood
@title:		Query NYT Article Search API
@date:		4/10/2015

# NYT API
	http://developer.nytimes.com/docs/read/article_search_api_v2

# Steps:
	1) Install urllib2, datetime, logging etc.
	2) Run 
		python nyt_v2.py
'''

# Import packages
import urllib2
import json
import datetime
import time
import sys, os
import logging
from urllib2 import HTTPError

# Set some vars.
api_key = 'put_api_key_here'

# Query
query = 'Budget+Deficit'

# Start and end dates
start = datetime.date(year = int(2015), month = int(2), day = int(1))
end   = datetime.date(year = int(2015), month = int(2), day = int(5))
  
# Open json file
outfile = open('out', 'w+')

# For iterating through dates
def daterange( start_date, end_date ):
	for n in range((end_date - start_date).days + 1):
		yield start_date + datetime.timedelta(n)

# Main Function
for date in daterange( start, end ):
	date = date.strftime("%Y%m%d")
	# NYT returns max of 101 pages for each day
	for page in range(2):
		try:
			request_string = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + query + "&begin_date=" + date + "&end_date=" + date + "&page=" + str(page) + "&api-key=" + api_key
			response = urllib2.urlopen(request_string)
			content = response.read()
			articles = json.loads(content)
			for article in articles['response']['docs']:
				print article['pub_date']
				outfile.write(article['pub_date']+'\n')
			# if no more articles, go to next date
			else:
				break
			time.sleep(5)
		except:
			continue

outfile.close()