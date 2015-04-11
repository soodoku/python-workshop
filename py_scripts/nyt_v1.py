'''

@author:	Gaurav Sood
@desc:		Query the nytimes article search API using the nytimesarticle package 
@date:		4/10/2015

# NYT API
	http://developer.nytimes.com/docs/read/article_search_api_v2

# nytimesarticle package
	https://pypi.python.org/pypi/nytimesarticle/0.1.0
	https://github.com/evansherlock/nytimesarticle/blob/master/README.txt
	
# Steps
	1) Install nytimesarticle
		python -m easy_install nytimesarticle
		pip install nytimesarticle
		
	2) Run 
		python nyt_v1.py
'''

# Import package
from nytimesarticle import articleAPI

# Set API Key
api = articleAPI('your_api_key')

# Query `bugdet deficits'
articles = api.search(q = 'federal budget deficits')

# articles = api.search(q = 'budget deficits', begin_date = 20111231, page=3)
# articles = api.search(q = 'budget deficits', fq = {'headline':'Obama'})

# Total hits
response = articles['response']['meta']['hits']
print response

# Get publication date of the articles
response = articles['response']['docs']
for item in response:
	print item['pub_date']
