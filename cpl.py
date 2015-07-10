# extracting candidates, including patterns and instances
import npc

# starting from a single category
data = ['John, mayor of New York, said New York is a great city']
patterns = ['mayor of']
instances = []
p_patterns = ['mayor of']
p_instances = []

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
	parts = s.split(ins)
	for part in parts:
		print part
		print npc.postag(part)
		if check(part):
			print pattern
			# preceding: [nouns] - verbs - adjectives/prepositions/determiners
			# preceding: nouns&adjectives - adjectives/prepositions/determiners
			# following: verbs - noun phrases/preposition
			p_patterns.append(pattern)			

def match(s, p): # match a single pattern
	print "in func: match string with pattern"
	if p in s:
		print "pattern found"
		x = s.split(p)[1]
		ps = npc.postag(x)
		if len(ps) == 0:
			return ""
		nps = npc.extNP(ps)
		if len(nps) == 0:
			return ""
		np = nps[0]
		print "found category instance: " + np
		p_instances.append([s, np])
		return np
	else:
		return ""		

if  __name__ == "__main__":
	print "in func: main"
	#match(data[0], p_patterns[0])
	get_patterns(data[0], "New York")
