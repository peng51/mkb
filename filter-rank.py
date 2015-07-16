# use coupled learning to filter patterns and instances
ratio = 0.75 # the ratio for filtering
num_patterns = 5 # the number of patterns to be promoted
num_instances = 100 # the number of instances to be promoted

# candidate pattern format
# {'2 mayor of': [('City', 'New York', 'sentence ...')]}
# promoted pattern format
# [('City', 2 mayor of')]
# candidate instance format
# {'New York': [('City', '2 mayor of', 'sentence ...')]}
# promoted instance format
# [('City', 'New York', 'sentence ....')]

def filter_instances(cins):
	print "in func: filter instances"
	fins = {}
	for ins in cins:
		# for each instance
		counts = {}
		n = 0.0
		# count the numbers for different categories
		for tup in cins[ins]:
			if tup[0] not in counts:
				counts[tup[0]] = 1.0
			else:
				counts[tup[0]] += 1.0
			n += 1.0
		cat = ''
		# filtering using ratio
		for x in counts:
			counts[x[0]] /= n
			if counts[x[0]] > ratio:
				cat = x[0]
				break
		if len(cat) != 0:
			fins[ins] = []
			for tup in cins[ins]:
				if tup[0] == cat:
					fins[ins].append(tup)
	return 	fins			
				
def rank_instances(fins):
	print "in func: rank instances"
	rins = tuple()
	# get the number of patterns for each instance
	for ins in fins:
		pats = set()
		for x in fins[ins]:
			if x[1] not in pats:
				pats.append(x[1])
		rins.append(ins, len(pats))
	# sort the ranked instances
	return sorted(rins, key=lambda tup: tup[1], reverse=True)

def promote_instances(fins, rins):
	print "in func: promote instances"
	pins = []
	# transform the format of promoted instances
	for i in range(num_instances):
		ins = rins[i][0]
		sens = fins[ins]
		for sen in sens:
			pins.append(sen[0], ins, sen[2])
	return pins

def filter_patterns(cpat):
	print "in func: filter patterns"
	fpat = {}
	ranks = []
	for pat in cpat:
		# for each instance
		counts = {}
		n = 0.0
		# count the numbers for different categories
		for tup in cpat[pat]:
			if tup[0] not in counts:
				counts[tup[0]] = 1.0
			else:
				counts[tup[0]] += 1.0
			n += 1.0
		cat = ''
		# filtering using ratio
		for x in counts:
			counts[x[0]] /= n
			if counts[x[0]] > ratio:
				cat = x[0]
				break
		if len(cat) != 0:
			fpat[pat] = cat
			ranks.append(pat, counts[pat])
	return fpat, pranks		

def rank_patterns(pranks):
	print "in func: rank patterns"
	return sorted(pranks, key=lambda tup: tup[1], reverse=True)	

def promote_patterns(fpat, pranks):
	print "in func: promote patterns"
	ppat = []
	# transform the format of promoted instances
	for i in range(num_patterns):
		pat = pranks[i][0]
		cat = fpat[pat]
		ppat.append(tuple(cat, pat))
	return ppat	