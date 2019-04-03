#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Date: Mon Mar 4 06:50:00 PDT 2019
# =============================================================================
"""
this module provide a way for searching file/folders, it offer two differents implementations
one implementation use 'find' command that scan the system at real time, the other is 'locate' command
that use its databases 
"""
# =============================================================================
# Imports
# =============================================================================
from os.path import normpath , join , isfile , isdir;
from re import escape;
from subprocess import Popen , PIPE;
 

def append(target="" , folder=None) :
	# if folder != None : return "'*/" + escape(normpath(join(folder, target))) + "'";
	# else : return "'*/" + escape(normpath(target)) + "'";
	if folder != None :
		s = normpath("/" + normpath(join(folder, target)))
		if len(s) > 1 and s[0] == s[1] == "/" : return "'*" + escape(s[1:]) + "'";
		else : return "'*" + escape(s) + "'"; 
	else : 
		s = normpath("/" + normpath(target));
		if len(s) > 1 and s[0] == s[1] == "/" : return "'*" + escape(s[1:]) + "'";
		else : return "'*" + escape(s) + "'";



def run(command , password=None) :
	if password != None :
		command = command.replace("sudo","echo {0} | sudo -S ".format(password))
	result = Popen(command , shell = True,stdout=PIPE,stderr=PIPE,stdin=PIPE)
	output , err = result.communicate()	
	print(command)
	#if result.returncode != 0 : raise ValueError("the query <{0}> can't work correctly".format(command))
	#its items cannot be "" or "\n" or any mix of them with any times, can be empty
	return [c for c in output.decode("utf-8").split("\n") if c.replace(" ","").replace("\n","") != ""];


def updateDb(password=None) :
	"""update the databased used by 'locate' command"""
	run("sudo updatedb" , password);


def lsearch(target="" , folder=None , _type="f") :
	"""
	search for file/folder in given path if found
	'target' is the file or folder to be searched it can be nested 
	eg : '/docs/file.txt' or simple item : 'file.txt'
	'folder' is the parent folder of the target and also it can be nested
	
	this function implemented with 'locate' it is much faster than fsearch, so it should be used if 
	a real time searching is not required	
	"""
	def detectType(s) :
		if _type == "f" : c = isfile;
		else : c = isdir;
		if s == [] : return [];
		return [i for i in s if c(i)];

	link = append(target , folder);
	print(link)
	return detectType(run("locate -i {0}".format(link) , None))


def fsearch(target="" , folder=None , _type="f" , password=None) :
	"""
	search for file/folder in given path if found
	'target' is the file or folder to be searched it can be nested 
	eg : '/docs/file.txt' or simple item : 'file.txt'
	'folder' is the parent folder of the target and also it can be nested
	'password' is the password for the root user

	this function implemented with 'find' it is slower than lsearch, so it should be used if 
	a real time searching is required   
	"""
	link = append(target , folder);
	print(link)
	return run("sudo find / -type {0} -ipath {1}".format(_type,link) , password=password)




# print(lsearch(target="monitor.py" , folder="v4" , _type="f"))
# print(fsearch(target="monitor.py" , folder="v4" , _type="f" , password="xcsd"))
