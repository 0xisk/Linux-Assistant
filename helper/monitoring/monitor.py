#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Kirollos Nasr Elias
# Created Date: Mon Mar 5 16:11:00 PDT 2019
# =============================================================================
"""
this module monitor the current running processes only that use the windows manager in a real time mode
"""
# =============================================================================
# Imports
# =============================================================================
from os import nice;
from os.path import split , expanduser;
from subprocess import Popen , PIPE;
from time import sleep;

#lower the priority of the task
try : nice(19);
except : pass;

#get the current logged in user
def getUserName() : return split(expanduser("~"))[-1];

def run(command , password=None) :
	"""
	'command' is any linux command in string to be executed even it requires a root user
	that is by give a password to 'password'
	return the stdout of the command ignoring stderr and stdin except for giving 'password' if it found.
	raising an ValueError exception on fail
	"""
	if password != None :
		command = command.replace("sudo","echo {0} | sudo -S ".format(password))
	result = Popen(command , shell = True,stdout=PIPE,stderr=PIPE,stdin=PIPE)
	output , err = result.communicate()	
	if result.returncode != 0 : raise ValueError("the query <{0}> can't work correctly".format(command))
	return output.decode("utf-8").split("\n");

#return the names of the processes
def getCurrentUIprocesses() : return (getUserName() , set([run("cat /proc/{0}/comm".format(c))[0].replace("\x00","") for c in run("wmctrl  -lp | awk  '{ print $3 }' | sort | uniq")[:-1]]));


#example of running
while True :
	print(getCurrentUIprocesses());
	sleep(0.6);
