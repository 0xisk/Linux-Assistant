from flask import Flask , jsonify , request;
from sklearn.externals.joblib import load;
from sys import argv;
from modules.run import run;
from modules import correct;
from dill import load as loading;
from sys import path;
from os.path import join , sep , isfile;

path.append("modules/monitoring")

from analysis import *;
from files import *;

def PATH() : return join(ROOTPATH , FOLDERNAME , Time.getYear() , Time.getMonth() , "log.csv");
rootFolder();
subContent();

ml = load("modules/models/model")
cv = load("modules/models/convertion")
cr = loading(open("modules/models/solving.bin","rb"));
fl = open(PATH() ,"a");

app = Flask(__name__);


def logData(query , reply , cmd) :
	global fl;

	def fileName(name) :
		parents = name.split(sep)[-3:][:-1]
		if parents[0] == Time.getYear() and parents[1] == Time.getMonth() : return True;
		return False;
	rootFolder();
	subContent();
	line = "{0},{1},{2},{3},{4}\n".format(query , reply , cmd , "{0}-{1}-{2}".format(Time.getYear() , Time.getMonth() , Time.getDay()) , Time.getTime());
	if not isfile(fl.name) or not fileName(fl.name) :
		fl = open(PATH() ,"a");
		fl.write(line);
		fl.flush();
		return;
	fl.write(line);
	fl.flush();


def predict(query) :
	classes = ['amixer -D pulse sset Master 50%+', 'amixer -D pulse sset Master 50%-', 'mkdir', 'mkdir -m 777', 'poweroff', 'reboot', 'systemctl suspend', 'eject', 'rm', 'rm -r']	
	(query , quotedwords) = correct.normalizeQuery(query , 0.55 , cr);
	query = [" ".join(query)];
	t_data  = cv.transform(query).toarray()
	result  = ml.predict(t_data)
	result  = result[0]
	cmd = classes[result];
	
	return cmd + " " + " ".join(quotedwords);


@app.route('/text' , methods=["POST"])
def text() :
	query = request.data.decode('utf-8')
	if query.replace(" ","") == "" : return "error has been detected";
	p = predict(query);
	try :
		run(p);
		logData(query , "jesus christ" , p);
	except : return "error has been detected"
	else :
		return p;


@app.route('/shutdown', methods=["GET"])
def shutdown():
	def shutdown_server():
		func = request.environ.get('werkzeug.server.shutdown')
		if func != None : func()
	shutdown_server();
	return "the server is shutting down.."


@app.route('/usage', methods=["GET"])
def getUsage() :
	return Collect().calculate();


@app.route("/test" , methods=["GET"])
def test() :
	return "jesus christ"



if __name__ == "__main__" :
	try :
		app.run(port = 9000 , debug = True);
	except : pass;