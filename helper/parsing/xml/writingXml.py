from thesaurus import Word;
from xmlparser import xmlParser;

#print(Word("become").synonyms(defnNum='all',relevance=[1,2,3]));


file = xmlParser("xml/xml.xml");
#file.appendCategory("become");




for relevent in Word("become").synonyms(defnNum='all',relevace=[1,2,3]) :
	for sub in relevent :
		file.appendWord("become",sub.replace("-"," "));



file.formateFile();
