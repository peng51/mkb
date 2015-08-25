import sys
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import mechanize
from bs4 import BeautifulSoup

num = 100
prefix = "http://www.google.com/images?oe=utf8&ie=utf8&source=uds&start=$start&hl=en&q=" # google image search link prefix
img_folder = 'images'

# initialize the google image search opener
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 
	'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]
#print opener.open("http://www.google.com/images?oe=utf8&ie=utf8&source=uds&start=$start&hl=en&q=apple").read();


def download(word): # download documents for a keyword
	senses = parse_senses(word)	
	# download documents for each sense
	for s in senses:
		print s
		doc = get_doc(prefix + s.replace(' ', '+'))
		download_images(doc, img_folder + '/' + word + '/' + s)

def parse_senses(word):
	print 'in func: parse_senses'
	senses = []
	url = prefix + word
	#print url
	doc = get_doc(url)
	soup = BeautifulSoup(doc)
	#print type(soup), len(soup)
	#print soup
	l = soup.find_all('a', {'class': 'rg_fbl'})
	for x in l:
		#print x['data-query']
		senses.append(x['data-query'])
	return senses

def get_urls():
	print 'in func: get_urls'


def get_doc(url):
	print 'in func: get_doc'	
	print url
	return opener.open(url).read()

def download_images(doc, path):
	print 'in func: get_images'
	soup = BeautifulSoup(doc)
	l = soup.find_all('a', {'class':'rg_l'})
	for x in l:
		print x['href']


if __name__ == '__main__':  
	download('apple')
