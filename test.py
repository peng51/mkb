# to test the correctness of extraction, filtering, ranking and promoting
import sys, os
import ext

# testing categories, PERSON, ANIMAL and LOCATON
tpatterns = [] # testingpatterns
categories = {}
max_init_num = 50 # the initial number of patterns

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
	s = f.readlines()[0]
	cins = ext.extract_instances(f, tpatterns)
	print len(cins)
	#print len(tpatterns)
	#for i in range(100):
	#	ext.match(s, tpatterns[i][1])


if __name__ == '__main__':
	#read_all_patterns("nellpatterns.csv", "somepatterns.csv")
	read_some_patterns('somepatterns.csv')
	test_pattern_matching('headlines.txt')