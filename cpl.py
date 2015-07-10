# extracting candidates, including patterns and instances
import npc

# starting from a single category
data = ['John, mayor of New York, said New York is a great city']
patterns = ['mayor of']
instances = []
promoted_patterns = ['mayor of']
promoted_instances = []

def single_extract_candidates(data):
	print "in func: singe_extract_candidates"	
	# extract category instances
	for p in promoted_patterns: 
		for s in data:
			match(s, p)
	# extract patterns
	for ins in promoted_instances:
		get_patterns(ins)		

def get_pattherns():
	print "test"
			

def match(s, p):
	print "in func: match string with pattern"
	if p in s:
		print "pattern found"
		x = s.split(p)[1]
		ps = npc.postag(x)
		np = npc.extNP(ps)[0]
		print "found category instance: " + np		

if  __name__ == "__main__":
	print "in func: main"
	match(data[0], promoted_patterns[0])

