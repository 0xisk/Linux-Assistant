from os import nice;
from os.path import split , expanduser;
from subprocess import Popen , PIPE;
from time import sleep;

try : nice(19);
except : pass;

def getUserName() : return split(expanduser("~"))[-1];

def run(command , password=None) :
	if password != None :
		command = command.replace("sudo","echo {0} | sudo -S ".format(password))
	result = Popen(command , shell = True,stdout=PIPE,stderr=PIPE,stdin=PIPE)
	output , err = result.communicate()	
	if result.returncode != 0 : raise ValueError("the query <{0}> can't work correctly".format(command))
	return output.decode("utf-8").split("\n");

def getCurrentUIprocesses() : return (getUserName() , set([run("cat /proc/{0}/comm".format(c))[0].replace("\x00","") for c in run("wmctrl  -lp | awk  '{ print $3 }' | sort | uniq")[:-1]]));

while True :
	print(getCurrentUIprocesses());
	sleep(0.6);
