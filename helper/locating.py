from subprocess import getoutput , Popen , PIPE;
from re import escape;
from os.path import isdir , isfile , join , normpath
from pathlib import Path;

class Locate :
	def __init__(self,password) :
		self.password = "'" + password + "'";

	def search(self,item,dest="''",type_="f") :
		def trim(path) :
			path = path[1:-1];
			if path != "" and path[0] == "/" : path = path[1:];
			if path != "" and path[-1] == "/" : path = path[:-1];
			if path.replace(" ","") == "" : return "";
			else :
				return escape(path);

		item = trim(item);
		dest = trim(dest);
		if dest == "" : quer = "'*/" + item + "'";
		else : quer = "'*/" + dest + "/" + item + "'";
		quer = "locate -i " + quer;
		print(quer)
		found = [];
		checker = None;
		if type_ == "f" : checker = isfile;
		elif type_ == "d" : checker = isdir;
		for itemPath in getoutput(quer).split("\n") :
			if checker(itemPath) : found.append(itemPath);
		return found;


	def updateDb(self) :
		command = ["updatedb"];
		p = Popen(['sudo', '-S'] + command, stdout=PIPE, stdin=PIPE, stderr=PIPE, universal_newlines=True)
		result = p.communicate(self.password + '\n')[0]





class Find :
	def __init__(self,password) :
		self.password = password

	def search(self,item,dest="''",type_="f") :
		def trim(path) : return path[1:-1];
			
		def run(arg,type_) :
			p = Popen(['sudo', '-S'] + ["find","/","-type",type_,"-iname",arg], stdout=PIPE, stdin=PIPE, stderr=PIPE, universal_newlines=True)
			result = p.communicate(self.password + '\n')[0]
			result = result.split("\n")
			try : result.remove("")
			except : pass; 
			return result;

		
		item = Path(item[1:-1]).parts;
		dest = Path(dest[1:-1]).parts;
		if item == () : return [];

		if len(dest) != 0 :
			if type_ == "f" : check = isfile;
			elif type_ == "d" : check = isdir; 
			output = [];
			result = run(dest[0],"d")
			if len(dest) > 1 :
				remain = join(*dest[1:]);
				for i in range(len(result)) :
					result[i] = join(result[i] , remain , join(*item));
					if check(result[i]) : output.append(result[i])
			else :
				print(result)
				for i in range(len(result)) :
					result[i] = join(result[i] , join(*item));
					print(result[i] , join(*item))
					if check(result[i]) : output.append(result[i])
		else :
			result = run(item[0],"f")
			if len(item) > 1 :
				remain = join(*item[1:]);
				for i in range(len(result)) :
					result[i] = join(result[i] , remain);
					if check(result[i]) : output.append(result[i])

		print(result)

#locate = Locate(password="jesus")

#print(locate.search("'var'",dest="'/'",type_="d"))
#locate.updateDb()


#find = Find(password="jesus")
#find.search("'search.py'",dest="''",type_="f")


def appendPathes(term="''" , dest="''") :
	def trim(path) :
		path = path[1:-1];
		path = path.replace('\\',"/");
		return path;

	term = trim(term);
	dest = trim(dest);
	if term == "" : return None;
	if dest == "" :
		if term[0] == "/" : term = term[1:];
	
	


appendPathes("'c'",dest="''")



