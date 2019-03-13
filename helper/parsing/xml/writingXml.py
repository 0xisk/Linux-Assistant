#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Date: Mon Feb 26 15:22:00 PDT 2019
# =============================================================================
"""
this module used to build a xml file, it use synonyms of a given word extracted from 'thesaurus' dictionary
"""
# =============================================================================
# Imports
# =============================================================================
from thesaurus import Word;
from xmlparser import xmlParser;


#appending the synonyms of a word 'become' as an example
"""
file = xmlParser("xml/xml.xml");
for relevent in Word("become").synonyms(defnNum='all',relevace=[1,2,3]) :
	for sub in relevent :
		file.appendWord("become",sub.replace("-"," "));

file.formateFile();
"""