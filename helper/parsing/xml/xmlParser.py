#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Kirollos Nasr Elias
# Created Date: Mon Feb 26 01:22:00 PDT 2019
# =============================================================================
"""
this module provide xmlParser class that can be used to buid or append an existing 
xml file, the structure of the file should have any number of categories elemets in
the root node, and each will have many words elements 
"""
# =============================================================================
# Imports
# =============================================================================
from xml.etree.ElementTree import parse , Element;
from os.path import isfile;
from vkbeautify import xml;
from datetime import datetime;

class xmlParser :
	"""xmlParser class used to build/append a xml file for an existed one"""
	def __init__(self,path) :
		""" 'path' should be string that represents a xml file path to be updated
		"""
		self.root = None;
		if isfile(path) :
			self.path = path;
			self.tree = parse(path)
			self.root = self.tree.getroot(); #get the root node of the xml structure


	def _getCategory(self,name) :
		"""'name' string represent the name of a category to be returned"""
		for cat in self.root :
			if cat.attrib["type"] == name :
				return cat;				


	def getCategoryValues(self,category) :
		"""return a set of all words text grouped in a category node 'category'"""
		cat = self._getCategory(category);
		if cat != None :
			names = set();
			for word in cat : names.add(word.text);
			return names #return set of all words in category 'category'

	def appendWord(self,category,value) :
		"""'value' is string represent a word to be added in 'category' category"""
		cat = self._getCategory(category);
		if cat != None :
			#create an element with name word
			element = Element("word")
			#give it a value of 'value' value
			element.text = value;
			#append it in the category 'cat'
			cat.append(element);
			#save updates
			try : self.tree.write(self.path, encoding="utf-8", xml_declaration=True);
			except : pass;



	def appendCategory(self,name) :
		"""append a category of name 'name'"""
		#create an element of name 'category', and of attribute 'type' of value 'name'
		element = Element("category",attrib={"type":name});
		element.text = " ";
		#append the category
		self.root.append(element);
		#save changes
		try : self.tree.write(self.path, encoding="utf-8", xml_declaration=True);
		except : pass;


	def formateFile(self) :
		"""formate the working xml file in a new xml file named the current date"""
		xml(self.path,str(datetime.now().time())+".xml");



#file = xmlParser("xml/dictionary.xml")
#file.appendCategory("inside");
#file.appendWord("inside" , "from")
#file.formateFile();

