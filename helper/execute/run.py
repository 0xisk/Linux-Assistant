#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Date: Mon Apr 1 03:10:00 PDT 2019
# =============================================================================
"""
this module provide an interface to run Linux commands, validate root user password
"""
# =============================================================================
# Imports
# =============================================================================
from subprocess import Popen , PIPE;

class WrongPasswordException(Exception) : 
	def __init__(self,password) : self.password = password;
	def __str__(self) : return "wrong password entered <{0}>".format(self.password);


def validatePassword(password) :
	"""password is a string represents the root user password.
	   this function return True if the password is correct or 'WrongPasswordException' exception 
	   is raised on failure
	"""
	try : run("sudo su",password);
	except ValueError : pass;
	else : return True; 
	raise WrongPasswordException(password);


def run(command , password=None) :
	"""
	'command' is any linux command in string to be executed even it requires a root user
	that is by giving a password to 'password'
	return the stdout of the command ignoring stderr and stdin except for giving 'password' if it found 
	"""
	if password != None :
		command = command.replace("sudo","echo {0} | sudo -S ".format(password), 1)#first occurance
	result = Popen(command , shell = True,stdout=PIPE,stderr=PIPE,stdin=PIPE)
	output , err = result.communicate()	
	if result.returncode != 0 : raise ValueError("the query <{0}> can't work correctly".format(command))
	return output.decode("utf-8")


# print(validatePassword("")) #validate the password

# run("amixer -D pulse sset Master 50%+")  #increase the volume by 50% 
# run("amixer -D pulse sset Master 50%-")  #decrease the volume by 50%
# run("suspend") 						   #suspend the computer
# run("reboot") 						   #reboot the computer
# run("poweroff") 						   #power off the computer
# run("sudo eject /dev/sdb","") 		   #eject a disk
