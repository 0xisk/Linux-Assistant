from sklearn.externals import joblib;
from re import sub;
from nltk.stem.porter import PorterStemmer;
from nltk.corpus import stopwords
from nltk import regexp_tokenize;
from sys import argv;
from run import run , validatePassword , WrongPasswordException;

def tokenize(text) :
	if text.replace(" ","") == "" : return [];
	return [word.lower() for word in regexp_tokenize(text, """("[^"]*"|[A-Za-z01-9%\'?']+)+""")];

def countQuoted(words) :
	coutnter = 0;
	q = None;
	for word in words : 
		if coutnter == 2 : return -2;
		if word.startswith('"') : coutnter += 1;q = word;
	if q == None : return -1;
	else : return q;

#loading models
ml=joblib.load("model")
cv=joblib.load("convertion")
ps = PorterStemmer()
print("\n\n")

password = input("your password : ");

while  True :
	take_input = input("\nyour query : ");
	review1 = tokenize(take_input);
	print(review1)
	f = countQuoted(review1)
	if f == -2 : print("can not have more than quoted words");exit(0)
	else : q = f;

	review1 = [ps.stem(word) for word in review1 if not word in set(stopwords.words('english'))]
	review1 = [' '.join(review1)]

	t_data  = cv.transform(review1).toarray()
	result  = ml.predict(t_data)
	result  = result[0]
	classes = ['amixer -D pulse sset Master 50%+', 'amixer -D pulse sset Master 50%-', 'mkdir', 'mkdir -m 777', 'poweroff', 'reboot', 'systemctl suspend', 'eject', 'rm', 'rm -r']

	cmd = classes[result];

	if cmd in ["rm" , "rm -r" , "mkdir" , "mkdir -m"] : 
		try :
			if q != None : cmd = cmd + " " + q
			print(cmd)
			print(run(cmd));
		except : print("nothing happened");
	else :
		try :
			print(run(cmd))
		except : print("nothing happened")

	print("-" * 40)

