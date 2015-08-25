import sys
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import mechanize
from bs4 import BeautifulSoup

num = 100

# initialize the google image search opener
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]
#print opener.open("http://www.google.com/images?oe=utf8&ie=utf8&source=uds&start=$start&hl=en&q=apple").read();


def download(word): # download documents for a keyword
	senses = parse_senses(word)	


	# download documents for each sense


def parse_senses(word):
	print 'in func: parse_senses'
	url = "http://www.google.com/images?oe=utf8&ie=utf8&source=uds&start=$start&hl=en&q=" + word
	print url

def get_urls():
	print 'in func: get_urls'

def get_doc(url):
	

if __name__ == '__main__':  
	download('apple')
	a = 1