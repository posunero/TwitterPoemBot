
class Counter:
	'''Constructor for counter

	dictionaries: ordered list of dictionaries to go through.  The
		algorithm scans through the list in the order that it's given in
	'''
	def __init__(self, dictionaries=['mhyph.txt']):
		self.dicts = []
		for d in dictionaries:
			f = open(d)
			words = {}
			for line in f:
				#count syllables
				#assume same syntax as the moby dictionary hyphenator
				syllables = line.count('\xa5') + 1
				word = line.replace('\xa5', '').strip().lower()
				words[word] = syllables
			self.dicts.append(words)
	def syllables(self, word):
		# first go through every dictionary 
		for d in self.dicts:
			if word in d:
				return d[word]
		# use heuristic if it's not in any dictionary
		if len(word)<3:
			return 1
		else:
			return 0 #temporary stub

def main():
	c = Counter()
	while True:
		i = raw_input('enter in a word to count syllables: ')
		print 'number of syllables: {0}'.format(c.syllables(i))
		
if __name__ == '__main__':
	main()

