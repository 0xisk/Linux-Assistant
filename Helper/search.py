#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Linux Assistant team
# Created Date: Mon Jan 19 18:54:00 PDT 2019
# =============================================================================
"""this module provide a class called 'search' that can be used under Linux platform
   to search for a file/dir through the system
"""
# =============================================================================
# Imports
# =============================================================================

from os.path import exists , join;
from subprocess import Popen, PIPE
from shlex import split;
from threading import Thread , Event;


class search :
	"""this class provide a tool to search for a file/dir starting from a given dir if found"""

	def __init__(self,name="",dirName=None,password="") :
		""" 
		name -> str , dirName -> str , password -> str

		'name' is the name of file/dir that need to be searched , 'dirName' is the dir
		from which the searching will start, if it is None(default) then the searching will start
		from the root folder, password is the current user password, if it is not correct an empty
		list will be the result usually  

		"""
		
		self.name = name;
		self.dirName = dirName;
		self.password = password;
		self.event = Event();
		self.countThreadsLives = 0;
		self.result = [];

	def runCommand(self,command) :
		"""
		'command' -> str 
		run 'find' command in an optimized way

		"""
		command = split(command)
		#split the command based on spaces, and pass it to be executed 
		p = Popen(['sudo', '-S'] + command, stdout=PIPE, stdin=PIPE, stderr=PIPE, universal_newlines=True)
		#communicate with the buffer to pass the password
		result = p.communicate(self.password + '\n')[0]
		result = result.split("\n")
		try : result.remove("") #remove any empty results if found
		except : pass; 
		#append the returned result to result
		self.result += result;
		self.countThreadsLives += 1;
		print(self.countThreadsLives)
		#this function will be executed twice at the same time, but we also need the total
		#result, so we don't return the result unless we are sure that it is executed two times
		#so if it reached '2', then we release the lock at 'parallel' function
		if self.countThreadsLives == 2 : self.event.set();


	def parallel(self,*funcs) :
		if len(funcs) == 0 : return;

		def startThread(func) :
			"this function start a new thread"
			thread = Thread(target=func,args=());
			thread.setDaemon(True);
			thread.start();

		event = Event();
		for i in range(len(funcs)) :
			if i == len(funcs) - 1 :
				startThread(funcs[i]);
			else : startThread(funcs[i]);
		self.event.wait(); #prevent the next line to be reached unless it will be released
		return


	def search(self) :
		"""this function start searching for the given file/dir"""
		if self.dirName == None :	#if dirName is None, then the searching will start from root folder
			if self.name.replace(" ","") != "" :
				path = self.name.split("/");
				path = [c for c in path if c != ""]; #split the name to be searched based on '/' 
				if path == [] : return [];
				pathes = [];
				#if the path of 'name' is only one name, then it may be file or dir
				#then we will search as it is a file or a dir at the same time 
				if len(path) == 1 : self.parallel(lambda : self.runCommand(("find -O3 / -type f -iname '"+path[0]+"'")) , lambda :  self.runCommand(("find -O3 / -type d -iname '"+path[0]+"'")));return self.result;
				else :
					#if it consists of more than one name, then it must be in form of: dir/dir/...file
					#self.parallel(self.runCommand(("find / -type f -iname '"+path[0]+"'")) , self.runCommand(("find / -type d -iname '"+path[0]+"'")))
					#so we will search for the first dir, then append each one from the result to what is
					#remained from the 'name', and consider each one is from the result if it exists
					pathes = [];
					self.runCommand(("find -O3 / -type d -iname '"+path[0]+"'"))
					for path_ in self.result :
						temp = join(path_,'/'.join(path[1:]));
						if exists(temp) : pathes.append(temp);
					return pathes;
			else :
				return [];
		elif self.dirName.replace(" ","") != "" :	#if 'dirName' is not None
			path = self.dirName.split("/");
			path = [c for c in path if c != ""];
			if path == [] : return [];
			pathes = [];
			#search for the first dir of the 'dirName', then append each result with what is remained 
			#from the 'dirName' also append each with the 'name'
			#and consider each one is from the result if it exists 
			self.runCommand(("find / -type d -iname '"+path[0]+"'"))
			for path_ in self.result :
				temp = join(join(path_,'/'.join(path[1:])) , self.name);
				if exists(temp) : pathes.append(temp);
			return pathes;





print(search(name="search.py",dirName="project",password="jesus").search());