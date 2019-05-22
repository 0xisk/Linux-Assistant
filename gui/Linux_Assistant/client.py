from json import dumps
from requests import post;
from sys import argv;
from modules.run import run;

userquery = argv[1];
if userquery.replace(" ","") == "" : exit(0);

url  = "http://localhost:9000/classify" 
data = dumps({"query" : userquery});

try :
	response = post(url , data);
except : exit(0);

if response.status_code != 404 :
	args = response.json()["args"]
	cmd  = response.json()["cmd"]

	if cmd != "NONE" : 
		print(cmd + " " + args)
		try :
			run(cmd + " " + args)
		except : exit(0);