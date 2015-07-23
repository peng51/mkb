# to test the correctness of extraction, filtering, ranking and promoting
import sys, os
import ext
import npc

# testing categories, PERSON, ANIMAL and LOCATON
tpatterns = [] # testingpatterns
categories = {}
max_init_num = 5000 # the initial number of patterns

#TODO: promoted patterns add confidence attribute
#TODO: recheck if new candidate patterns are required to extract only from promoted instances sentences or all possible sentences

def read_all_patterns(filename, somename):
	print "in func: read_patterns"
	f = open(filename, 'r')
	no = 0
	sps = []
	for line in f:
		labels = line.split('\t')
		if labels[0] == 'person' and labels[1] == 'extractionpatterns':
			sps.append(line)
		elif labels[0] == 'animal' and labels[1] == 'extractionpatterns':
			sps.append(line)
		elif labels[0] == 'city' and labels[1] == 'extractionpatterns':
			sps.append(line)

		if labels[0] not in categories:
			categories[labels[0]] = 1
		else:
			categories[labels[0]] += 1
	f.close()
			
	print len(categories)
	print len(sps)
	g = open(somename, 'w')
	for x in sps:
		g.write(x)
	g.close()
		
def read_some_patterns(filename):
	print "in func: read_some_patterns"
	f = open(filename, 'r')
	pno, ano, cno = 0, 0, 0
	for line in f:
		labels = line.split('\t')
		#print line
		if labels[0] == 'person' and pno < max_init_num:
			tpatterns.append((labels[0], labels[2]))
			pno += 1
			#print line
		elif labels[0] == 'animal' and ano < max_init_num:
			tpatterns.append((labels[0], labels[2]))
			ano += 1
			#print line
		elif labels[0] == 'city' and cno < max_init_num:
			tpatterns.append((labels[0], labels[2]))
			cno += 1
			#print line
	#print tpatterns		
			
def test_pattern_matching(tdata): # tdata for testing headlines data
	print "in func: test_pattern_matching"
	f = open(tdata, 'r')
	data = f.readlines()
	print len(tpatterns), len(data)
	cins = ext.extract_instances(data, tpatterns)
	print len(cins)

def test_extract_instances():
	read_some_patterns('somepatterns.csv')
	test_pattern_matching('headlines.txt')

def test_extract_patterns():
	print "in func: test_extract_patterns"
	pins = []
	f = open('seeds-ins.txt', 'r')
	for line in f:
		cs = line[:-1].split('\t')
		tup = cs[0], cs[1], cs[2]
		pins.append(tup)
	cpat = ext.extract_patterns(pins)
	print len(cpat)
	#for x in cpat:
		#print x, '\t', cpat[x]


if __name__ == '__main__':
	#read_all_patterns("nellpatterns.csv", "somepatterns.csv")
	#test_extract_instances()
	test_extract_patterns()
