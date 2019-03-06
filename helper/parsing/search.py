#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Kirollos Nasr Elias
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
	"""
	'command' is any linux command in string to be executed even it requires a root user
	that is by give a password to 'password'
	return the stdout of the command ignoring stderr and stdin except for giving 'password' if it found 
	"""
	if password != None :
		command = command.replace("sudo","echo {0} | sudo -S ".format(password))
	result = Popen(command , shell = True,stdout=PIPE,stderr=PIPE,stdin=PIPE)
	output , err = result.communicate()	
	#if result.returncode != 0 : raise ValueError("the query <{0}> can't work correctly".format(command))
	return output


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
	return detectType(run("locate -i {0}".format(link) , None).decode("utf-8").split("\n")[:-1]);


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
	return run("sudo find / -type {0} -ipath {1}".format(_type,link) , password=password).decode("utf-8").split("\n")[:-1];





