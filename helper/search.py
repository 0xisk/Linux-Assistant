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
	#if result.returncode != 0 : raise ValueError("the query <{0}> can't work correctly".format(command))
	return output

def updateDb(password=None) :
	run("sudo updatedb" , password);


def lsearch(target="" , folder=None , _type="f" , password=None) :
	def detectType(s) :
		if _type == "f" : c = isfile;
		else : c = isdir;
		if s == [] : return [];
		return [i for i in s if c(i)];

	link = append(target , folder);
	print(link)
	return detectType(run("locate -i {0}".format(link) , password=password).decode("utf-8").split("\n")[:-1]);


def fsearch(target="" , folder=None , _type="f" , password=None) :
	link = append(target , folder);
	print(link)
	return run("sudo find / -type {0} -ipath {1}".format(_type,link) , password=password).decode("utf-8").split("\n")[:-1];





