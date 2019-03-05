#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Linux Assistant team
# Created Date: Mon Jan 21 01:22:00 PDT 2019
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
		""" path -> str
			'path' is the path of the xml file to be built/appended
		"""
		self.root = None;
		if isfile(path) :
			self.path = path;
			self.tree = parse(path)
			self.root = self.tree.getroot(); #get the root node of the xml structure


	def _getCategory(self,name) :
		"""return the node that is the category named 'name'"""
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
		"append a word with name 'value' in a category named 'category'"
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
		"create a xml file as a well formatted version of the opened xml file of name is the current date"
		xml(self.path,str(datetime.now().time())+".xml");



#file = xmlParser("xml/dictionary.xml")
#file.appendCategory("inside");
#file.appendWord("inside" , "from")
#file.formateFile();

