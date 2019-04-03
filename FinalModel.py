from sklearn.externals import joblib
import re
from nltk.stem.porter import PorterStemmer

ml=joblib.load('ML_Model')


take_input = input('Enter your text: ')
review1 = re.sub('[^a-zA-Z]', ' ', take_input)
review1 = review1.lower()
review1 = review1.split()
ps = PorterStemmer()
review1 = [ps.stem(word) for word in review1 if not word in set(stopwords.words('english'))]
review1 = ' '.join(review1)
review1=[review1]
#review1 = cv.fit_transform(review1).toarray()
t_data=cv.transform(review1).toarray()
result=ml.predict(t_data)
result=result[0]
classes=['amixer -D pulse sset Master 50%+', 'amixer -D pulse sset Master 50%-', 'mkdir', 'mkdir -m 777', 'poweroff', 'reboot', 'systemctl suspend', 'eject', 'rm', 'rm -r']

print(classes[result])


