from nltk import regexp_tokenize;
from nltk import RegexpParser;
from pattern.en import tag;

dictionary = ["file","named","folder"]; #sample of dictionary

def tokenize(text) :
	"tokenize a sentence based on spaces or double-quoted words"
	if text.replace(" ","") == "" : return [];
	return regexp_tokenize(text, """("[^"]*"|[A-Za-z\'?']+)+""");


def pos(text) :
	""" text -> str
		used to label every token in a list of tokens with part of speech tag 
	"""
	#tokenize the given sentence
	tokens = tokenize(text);
	tagged = [];
	for token in tokens :
		#for every token, if it found in the dictionary, then do nothing
		if token in dictionary : continue;
		#get POS of a token as a tuple of its value and the corresponding POS
		result = tag(token)
		if len(result) > 1 :
			#if the list has more than one tuple, which means that, this is a sentence, so it will considered
			#as a NN
			tagged.append( ((" ".join([i[0] for i in result if i[0] != '"'])) , "NN") );
		else :
			#if the list has only one tuple, then simply append it
			tagged.append(tag(token)[0]);
	return tagged


def obtain(text,grammar) :
	""" text -> str , grammer -> str
		it will compare the grammer of the 'text', if it follow the grammer 'grammer', if true
		then it will extract some tokens from it 
	"""
	if grammar.replace(" ","") == "" or text.replace(" ","") == "" : return [];
	#build a grammer chunker
	chunker = RegexpParser(grammar);
	#get the POS of query tokens
	tagged = pos(text)
	#get trees of matched sentences
	chunked = chunker.parse(tagged);
	#if any tree found in the loop, then there are matched trees
	for tree in chunked.subtrees() :
		if tree.label() == "ORDERED" : 
			return [tagged[0][0] , tagged[1][0] , tagged[3][0]];
		if tree.label() == "UNORDERED" :
			return [tagged[2][0] , tagged[3][0] , tagged[1][0]];

#print(pos('delete file "music file name" from musics'))


print(obtain('delete file "music file name" from folder musics' , 
	"""
	ORDERED: {<VB.?><NN.?>(<IN><NN.?>)?} 
	UNORDERED: {(<IN><NN.?>)?<VB.?><NN.?>}
	"""));
