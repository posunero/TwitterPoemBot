from sylla import Counter
import unittest

class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		self.counter = Counter()
	def test_words(self):
		tc = open('cases.txt')
		for line in tc:
			# format is: word syllables
			ls = line.split()
			word = ls[0]
			syllables = int(ls[1])
			print "word, syllables: ", word, syllables
			self.assertEqual(self.counter.syllables(word), syllables)

if __name__ == '__main__':
	unittest.main()
