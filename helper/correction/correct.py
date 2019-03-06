#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Kirollos Nasr Elias
# Created Date: Mon Mar  18:54:00 PDT 2019
# =============================================================================
"""this module provide a way to give suggestions of each query to be written
   'Suggestion' class's 'suggest' must be used when each character written by the user, and 
   it will return a list of all possible words
"""
# =============================================================================
# Imports
# =============================================================================
from enchant import Dict;
from contractions import fix;

class Suggestion :
	def __init__(self) :
		self._suggester = Dict("en_US");

	def suggest(self,word) :
		"""
		'word' should be string, that represents a part of word where suggestions will be buit based on it
		return a list of suggestions or empty list
		"""
		self._suggester.check(word); 
		return self._suggester.suggest(word);


class Contraction :
	@staticmethod
	def solve(sentence) :
		"""'sentence' should be string, where all contractions and slangs will be converted to a formal form
		   return string represent the 'sentence' after correction
		"""		
		return fix(sentence);



#print(Suggestion().suggest("delte"))
#print(Contraction().solve('I\'m here and wanna remove this file that\'s named "file name"'))