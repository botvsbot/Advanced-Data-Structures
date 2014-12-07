# A basic trie with insert, search and delete operations

import time

class Trie(object):

	def __init__(self):
		self.word = None
		self.children = {}

	def insert(self, word):
		for letter in word.lower():
			if letter not in self.children:
				self.children[letter] = Trie()
			self = self.children[letter]
		self.word = word

	def search(self, word):
		for letter in word.lower():
			if letter not in self.children:
				return False
			self = self.children[letter]
		return (self.word != None)
        
	def delete(self, word):
		deepest_tree = self
		suffix = ""
		for letter in word.lower():
			if letter not in self.children:
				return # the word to be deleted is not in the trie
			if self.word != None or len(self.children) > 1: # A possible prefix exists to the word to be deleted
				deepest_tree = self
				suffix = letter
			else:
				suffix = suffix+letter
			self = self.children[letter]
		if self.word == word:
			if not self.children: # the word is not a prefix of an existing word
				for i in xrange(0, len(suffix) - 1):
                        		if i < len(suffix)-2:
                            			grand_child = (deepest_tree.children[suffix[0]]).children[suffix[i+1]].children[suffix[i+2]]
                            			deepest_tree.children[suffix[0]].children[suffix[i+2]] = grand_child
                            			if suffix[i+2] == suffix[i+1]:
                                			continue
                        		del(deepest_tree.children[suffix[0]].children[suffix[i+1]])
                    		del(deepest_tree.children[suffix[0]])
			else: # the word is a prefix of another word in the trie
				self.word = None
		else:
			return # the word to be deleted is not in the trie


trie = Trie()
words = "the their there they hi sup know knowing".split(" ")
for word in words:
  trie.insert(word)
trie.search("there")
trie.delete("there")
trie.search("they")
