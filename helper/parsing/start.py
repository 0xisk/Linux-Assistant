#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Linux Assistant team
# Created Date: Mon Jan 20 06:50:00 PDT 2019
# =============================================================================
"""
this module provide 'find' class to analyse user query and execute the corresponding linux command
the commands will be related to file/dir manipulations on Linux platform
"""

from intro import App;
from time import sleep;

#start loading screen
app = App();

print("jesus christ")

from nltk import Text , regexp_tokenize;
from pattern.en import lemma
from os.path import isdir , isfile;
from pickle import load;
from search import search;

print("1")

def colModelLoad(path) :
	"loads collocation model that is pickled at 'path', then return it or False on failure"
	if isfile(path) :
		with open(path , "rb") as file :
			return load(file);
	else : return False;

print("2")

def anaModelLoad() :
	"load en_coref_[sm|md|lg] model to resolve anaphora, then return it"
	from spacy import load;
	nlp = load("en_coref_lg");
	return nlp;

#load collocation model	
COLMODEL = colModelLoad("../../model/collocationDetectorModel.sav");
print(COLMODEL)
#load anaphora resolution model
#ANAMODEL = anaModelLoad();

print("3")

class find :
	"""this class will analyse the user query and tries to correspond it to the intended command"""
	dictionary = ["create","remove","delete","cut out","from","in","inside"]; #dic sample
	def __init__(self , text) :
		"""
		'text' -> str

		'text' is the user query, that typically describes a linux command  
		"""
		
		#m = ANAMODEL(text);
		#if m._.has_coref : self.text = m._.coref_resolved;
		#else : self.text = text;
		#print(self.text)
		
		#split the user query into tokens based on a rule
		self.tokenized = self.tokenize(text);	
		#detect the 'OREDERED' collocation statements
		self.detectCollocations();
		#filter the tokens from any words that is not found in the dictionary
		self.filterText();

	def splitByName(self) :
		"""this function return a list of list, each one considred as a group"""
		splitted = [[]]; #started with an empty list
		for token in self.tokenized :
			#lowercase each token
			token = token.lower();
			if not token.startswith('"') :
				#each token that is not quoted, will be normalized, then added to the last list
				token = lemma(token);
				splitted[-1].append(token);
			#if a quoted token is found, then it will added as a single-token group, then an empty list
			#added at the last
			else : splitted.append([token]);splitted.append([]);
		try :
			splitted = [c for c in splitted if c != []];
		except : pass;
		finally : return splitted;

	@staticmethod
	def tokenize(text) :
		if text.replace(" ","") == "" : return [];
		return regexp_tokenize(text, """("[^"]*"|[A-Za-z\'?']+)+""");

	def detectCollocations(self) :
		"""used to detect collocation(2/3gram) from a list of tokens"""
		#if the model is well loaded, then it will be used otherwise the function terminates
		if COLMODEL == False : return;
		#the tokenized user query will be grouped, each group is a either a quoted token only or
		#some tokens, if the length of a group is more than one, then it will be checked for collocation 
		splitted = self.splitByName()
		for i in range(len(splitted)) :
			if len(splitted[i]) > 1 : splitted[i] = [c.replace("_"," ") for c in COLMODEL[1][COLMODEL[0][splitted[i]]]];
		self.tokenized = sum(splitted,[]);

	def filterText(self) :
		"update the tokenized query to be filtered from any words except what is found at the dictionary"
		self.tokenized = [c for c in self.tokenized if c in self.dictionary or c.startswith('"')];
		print(self.tokenized);



from tkinter import Tk , LabelFrame , Entry , Button , Label;

class MainWin(Tk) :
	def __init__(self,title) :
		Tk.__init__(self);
		self.title(title);
		self.geometry("600x200")
		self.columnconfigure(0,weight=1)
		self.rowconfigure(1,weight=1);
		self._upperPart();
		self._lowerPart()
		self.bind("<Return>",lambda event : self._onClick());


	def _upperPart(self) :
		lblframe = LabelFrame(self,text="Query");
		lblframe.columnconfigure(0,weight=1)
		lblframe.grid(row=0,column=0,padx=10,pady=10,ipadx=10,ipady=10,sticky="snew");
		self.queryEntry = Entry(lblframe,font=("consolas",12))
		self.queryEntry.grid(row=0,column=0,padx=10,pady=(10,5),ipady=1,sticky="snew");
		self.goButton = Button(lblframe,text="Go",bg="grey",fg="#FFF",width=10,command=self._onClick);
		self.goButton.grid(row=0,column=1,padx=10,pady=(10,5),ipady=2,sticky="we");


	def _lowerPart(self) :
		lblframe = LabelFrame(self,text="Output");
		lblframe.columnconfigure(0,weight=1)
		lblframe.rowconfigure(0,weight=1)
		lblframe.grid(row=1,column=0,padx=10,pady=(5,10),ipadx=10,ipady=10,sticky="snew");
		self.output = Label(lblframe,text="jesus christ",anchor="nw");
		self.output.grid(row=0,column=0,padx=5,pady=5,sticky="snew")

	def _onClick(self) :
		query = self.queryEntry.get();
		if query.replace(" ","") == "" or len(query.split(" ")) == 1 : return;
		else :
			self.output.configure(text=' '.join(find(query).tokenized))
		


	def run(self) :
		self.mainloop();


#end loading screen
app.callback();



MainWin("jesus christ").run();







