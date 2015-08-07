# extracting candidates, including patterns and instances
import npc

# starting from a single category
data = ['John, mayor of New York, said New York is a great city']
p_patterns = ['2 mayor of']

dt = 'DT'
prep = 'IN'
noun = 'NN'
nouns = 'NNS'
verb = 'VB'
adj = 'JJ'

def single_extract_candidates(data):
	print "in func: singe_extract_candidates"	
	# extract category instances
	for p in promoted_patterns: 
		for s in data:
			match(s, p)
	# extract patterns
	for ins in promoted_instances:
		get_patterns(ins)

def test():
	#s = "New mayor of Westhoughton's special way to celebrate a special year"
	#print s
	#print npc.postag(s)
	#print get_patterns(s, 'Westhoughton')
	print match('Best Western Hotel Merian am Rhein Accommodation', '_ am Rhein')		

def extract_patterns(pins):
	print "in func: extract_patterns"
	cpat = {} # candidate instances
	for ins in pins:
		#print ins[2]
		#print npc.postag(ins[2])
		ps = get_patterns(ins[2], ins[1])	
		if len(ps) == 0:
			continue
		for p in ps:
			if p not in cpat:
				cpat[p] = []
				newtuple = ins[0], ins[1], ins[2]
				cpat[p].append(newtuple)
			else:
				newtuple = ins[0], ins[1], ins[2]
				cpat[p].append(newtuple)
	return cpat		

def get_mentions(ps, ip):
	ms = []
	i = 0
	while i < len(ps):
		if ps[i][0] == ip[0][0]:
			j = i
			while j < len(ps) and j - i < len(ip):
				if ps[j][0] != ip[j - i][0]:
					break
				j += 1
			if j - i == len(ip):
				ms.append(i)
				i = j
			else:
				i += 1
		else:
			i += 1
	return ms

def get_patterns(s, ins):
	# preceding patterns empty room, optionally or non-optionally 
	# print "preceding: [nouns] - verbs - adjectives/prepositions/determiners"
	# print "preceding: nouns&adjectives - adjectives/prepositions/determiners"
	# print "following: verbs - noun phrases/preposition"
	ps = npc.postag(s)
	ip = npc.postag(ins)
	ms = get_mentions(ps, ip)
	#print len(ms)
	patterns = []
	p = 0
	l = len(ps) - 1
	#print len(ms)
	for i in range(len(ms)):
		b = ms[i]
		e = b + len(ip)
		if i < len(ms) - 1:
			l = ms[i + 1] - 1
		else:
			l = len(ps) - 1
		p1 = ext1rule(ps, p, b - 1)
		p2 = ext2rule(ps, p, b - 1)
		p3 = ext3rule(ps, e, l)
		if len(p1) != 0: 
			patterns.append(p1 + ' _')
			#print "p1", p1
		if len(p2) != 0: 
			patterns.append(p2 + ' _')
			#print "p2", p2
		if len(p3) != 0: 
			patterns.append('_ ' + p3)
			#print "p3", p3
		# update p and l
		p = e

	return patterns

def ext1rule(ps, b, e):
	s = []
	x = -1
	for i in range(e, b - 1, -1):
		if 'VB' in ps[i][1]:
			s.append(ps[i][0])
			x = i
			break 
		elif 'DT' in ps[i][1] or 'JJ' in ps[i][1] or 'IN' in ps[i][1]:
			s.append(ps[i][0])
		else:
			break
	if x == -1: return ''
	# modify this rule to add noun phrases
	i = x - 1
	while i >= b: # the state-machine
		if 'VB' in ps[i][1]: 
			s.append(ps[i][0])
			i -= 1
		elif ps[i][1] == 'NN' or ps[i][1] == 'NNS':
			s.append(ps[i][0])
			break
		elif 'NNP' in ps[i][1]:
			j = i
			while j >= b and 'NNP' in ps[j][1]:
				s.append(ps[j][0])
				j -= 1
			break
		else:
			break

	if len(s) == 0: return ''
	else: 
		t = ''
		for i in range(len(s) - 1, -1, -1):
			t += s[i] + ' '
		return t[:len(t) - 1]			 		

def ext2rule(ps, b, e):
	s = []
	i = e
	foundN = False
	while i >= b: # the state-machine
		if 'VB' in ps[i][1]: 
			break
		elif 'DT' in ps[i][1] or 'JJ' in ps[i][1] or 'IN' in ps[i][1]:
			s.append(ps[i][0])
			i -= 1
		elif ps[i][1] == 'NN' or ps[i][1] == 'NNS':
			s.append(ps[i][0])
			foundN = True
			break
		elif 'NNP' in ps[i][1]:
			foundN = True
			j = i
			while j >= b and 'NNP' in ps[j][1]:
				s.append(ps[j][0])
				j -= 1
			break
		else:
			break
	#print s
	if len(s) == 0 or not foundN: return ''
	else: 
		t = ''
		for i in range(len(s) - 1, -1, -1):
			t += s[i] + ' '
		return t[:len(t) - 1]

def ext3rule(ps, b, e):
	s = ''
	for i in range(b, e + 1):
		if ('VB' in ps[i][1]):
			s += ps[i][0] + " "
		elif len(s) != 0 and ps[i][1] == 'IN':
			s += ps[i][0] + " "
		elif len(s) != 0 and 'NN' in ps[i][1]:
			s += ps[i][0] + " "
			break
		elif len(s) != 0 and 'NNP' in ps[i][1]:
			j = i
			while j <= e and 'NNP' in ps[j][1]:
				s += ps[j][0] + " "
				j += 1
			break
		else:
			break
	if len(s) == 0: return s
	else: return s[:len(s) - 1]

def match(s, p): # match a single pattern, return the noun phrase
	#print "in func: match string with pattern"
	#TODO: for future improvement, using getMentions instead
	t = '0'
	if p.find('_') == 0:
		t = 'h'
		p = ' ' + p[2:] + ' '
	else:
		t = 't'
		p = ' ' + p[0:-2] + ' '
	#print t, p
	if p in s:
		#print "pattern found"
		if t == 't':
			x = s.split(p)[1]
			ps = npc.postag(x)
			np = npc.extFirstNP(ps)
			return np
		else:
			x = s.split(p)[0]
			ps = npc.postag(x)
			np = npc.extLastNP(ps)
			return np				
	else:
		return ""		

	
def extract_instances(data, ppat):
	# data structure, instance - category - patterns, dictionary - list of tuples
	print "in func: extract_instances"
	cins = {} # candidate instances
	#print len(data)
	no = 0
	for s in data:
		s = unicode(s[:-1], errors="ignore") # encode the string as unicode to deal with outliers
		for p in ppat:
			#up = unicode(p, errors="ignore")
			cat = p[0] # category
			pat = unicode(p[1], errors="ignore") # pattern
			ins = match(s, pat)
			if len(ins) != 0:
				print ins + '\t' + p[0] + ', ' + p[1] + '\t' + s 
				if ins in cins:
					intuple = p[0], p[1], s
					cins[ins].append(intuple)
				else:
					cins[ins] = []
					intuple = p[0], p[1], s
					cins[ins].append(intuple)
		no += 1
		if no % 10000 == 0:
			print no, 'lines processed'
	return cins

		

def extract(data, ppat, pins): 
	# data - the whole dataset; ppat - promoted patterns; pins - promoted instances and associated data
	# extract candidate instances
	extract_instances(data, ppat)
	# extract candidate patterns
	extract_patterns(pins)
			

if  __name__ == "__main__":
	print "in func: main"
	test()
	#print npc.postag("being acquired by Google")
	#match(data[0], p_patterns[0])
	#get_patterns(data[0], "New York")
