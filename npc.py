import nltk, re, pprint
import os
import sys
import codecs
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import PorterStemmer

wnl = WordNetLemmatizer() # lemmatizer
st = PorterStemmer()

def read_file(filename):
	print "reading file"
	f = open(filename,'r')
	docs = []
	for line in f:
		docs.append(unicode(line, errors="ignore"))
	return docs	

def extract(docs):# extract named entities and noun phrases
	print "extracting noun phrases"
	for s in docs:
		# tokenization, pos tagging, named entity extraction
		ws = nltk.word_tokenize(s)
		ps = nltk.pos_tag(ws)
		ns = nltk.ne_chunk(ps)
		ns = nltk.ne_chunk(ps, binary=True)
		# extract noun phrases and entities
		nps = extNP(ps)
		return nps

def extNP(ps): # extract NP
	nps = []
	i = 0
	while i < len(ps):
		x = ps[i]
		if x[1] == 'NN' or x[1] == 'NNS':
			y = wnl.lemmatize(x[0])
			nps.append(y)
			#nps.append(x[0])
			i += 1
		elif x[1] == 'NNP' or x[1] == 'NNPS':	
			np = ''
			while i < len(ps) and (ps[i][1] == 'NNP' or ps[i][1] == 'NNPS'):
				np += wnl.lemmatize(ps[i][0]) + " "
				#np += ps[i][0] + " "
				i += 1
			nps.append(np[:len(np) - 1])

		else:
			i += 1
	return nps	

