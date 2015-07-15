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

def get_patterns(s, ins):
	# preceding patterns empty room, optionally or non-optionally 
	# print "preceding: [nouns] - verbs - adjectives/prepositions/determiners"
	# print "preceding: nouns&adjectives - adjectives/prepositions/determiners"
	# print "following: verbs - noun phrases/preposition"
	parts = s.split(ins)
	patterns = []
	for i in range(len(parts)):
		part = parts[i]
		#print part
		ptag = npc.postag(part)
		# print ptag
		if i < len(parts) - 1:
			p1 = ext1rule(ptag)
			p2 = ext2rule(ptag)
			if len(p1) != 0: patterns.append('1 ' + p1)
			if len(p2) != 0: patterns.append('2 ' + p2)
		if i > 0:	
			p3 = ext3rule(ptag)
			if len(p3) != 0: patterns.append('3 ' + p3)
	print "pattens extracted: "
	for p in patterns:
		print p
	return patterns

def ext1rule(ptag):
	s = []
	x = -1
	for i in range(len(ptag) - 1, -1, -1):
		if 'VB' in ptag[i][1]:
			s.append(ptag[i][0])
			x = i
			break 
		elif 'DT' in ptag[i][1] or 'JJ' in ptag[i][1] or 'IN' in ptag[i][1]:
			s.append(ptag[i][0])
		else:
			break
	if x == -1: return ''
	for i in range(x - 1, -1, -1):
		if ptag[i][1] == 'NN' or ptag[i][1] == 'NNS':
			s.append(ptag[i][0])
			break
		elif 'VB' in ptag[i][1]: 
			s.append(ptag[i][0])
		else:
			break	
	if len(s) == 0: return ''
	else: 
		t = ''
		for i in range(len(s) - 1, -1, -1):
			t += s[i] + ' '
		return t[:len(t) - 1]
	#x = -1
	#for i in range(len(ptag)):
	#	#print ptag[i][0], ptag[i][1]
	#	if 'VB' in ptag[i][1]:
	#		x = i
	#		break
	#if x == -1: return ''
	#s = ''
	#if x > 0 and (ptag[x - 1][1] == 'NN' or ptag[x - 1][1] == 'NNS'):
	#		s += ptag[x - 1][0] + " "
	#s += ptag[x][0] + " "
	#for i in range(x + 1, len(ptag)):
	#	if 'VB' in ptag[i][1] or 'DT' in ptag[i][1] or 'JJ' in ptag[i][1] or 'IN' in ptag[i][1]:
	#		s += ptag[i][0] + " "
	#	else:
	#		#return ""
	#		break
	#if len(s) == 0: return s
	#else: return s[:len(s) - 1]			 		

def ext2rule(ptag):
	s = []
	for i in range(len(ptag) - 1, -1, -1):
		if 'VB' in ptag[i][1]:
			return ''
		elif ptag[i][1] == 'NN' or ptag[i][1] == "NNS":
			s.append(ptag[i][0])
			break
		elif 'DT' in ptag[i][1] or 'JJ' in ptag[i][1] or 'IN' in ptag[i][1]:
			s.append(ptag[i][0])
		else:
			break
	if len(s) == 0: return ''
	else: 
		t = ''
		for i in range(len(s) - 1, -1, -1):
			t += s[i] + ' '
		return t[:len(t) - 1]
	#x = -1
	#for i in range(len(ptag)):
	#	#print ptag[i][0], ptag[i][1]
	#	if 'VB' in ptag[i][1]:
	#		return ""
	#	if ptag[i][1] == 'NN' or ptag[i][1] == "NNS":
	#		x = i
	#		break
	#if x == -1: return ''
	#s = ptag[x][0] + " "
	#for i in range(x + 1, len(ptag)):
	#	if 'DT' in ptag[i][1] or 'JJ' in ptag[i][1] or 'IN' in ptag[i][1]:
	#		s += ptag[i][0] + " "
	#	else:
			#return ""
	#		break
	#if len(s) == 0: return s
	#else: return s[:len(s) - 1]	
	

def ext3rule(ptag):
	s = ''
	for i in range(len(ptag)):
		if ('VB' in ptag[i][1]):
			s += ptag[i][0] + " "
		elif len(s) != 0 and ptag[i][1] == 'IN':
			s += ptag[i][0] + " "
		else:
			break
	if len(s) == 0: return s
	else: return s[:len(s) - 1]

def match(s, p): # match a single pattern
	print "in func: match string with pattern"
	print p
	t = p[0]
	p = p[2:]
	print t, p
	if p in s:
		print "pattern found"
		if t == '1' or t == '2':
			x = s.split(p)[1]
			ps = npc.postag(x)
			if len(ps) == 0:
				return []
			nps = npc.extNP(ps)
			if len(nps) == 0:
				return []
			np = nps[0]
			print "found category instance: " + np
			#p_instances.append([s, np])
			return [s, np]
		else:
			x = s.split(p)[0]
			ps = npc.postag(x)
			if len(ps) == 0:
				return []
			nps = npc.extNP(ps)
			if len(nps) == 0:
				return []
			np = nps[len(nps) - 1]
			print "found category instance: " + np
			return [s, np]
					
	else:
		return []		

if  __name__ == "__main__":
	print "in func: main"
	#print npc.postag("being acquired by Google")
	match(data[0], p_patterns[0])
	get_patterns(data[0], "New York")
