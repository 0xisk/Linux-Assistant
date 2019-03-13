import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
nltk.download('stopwords')



#Reading The Dataset
dataset = pd.read_csv('dataset.csv')

# Cleaning the texts
corpus = []
for i in range(0,17760):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Text'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
#Count vextorizations
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)




#Splinting the dataset to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state =1)





#SVC Classification
svc = SVC(kernel='sigmoid', gamma=1.0)
svc.fit(X_train, y_train)
prediction = svc.predict(X_test)

accuracy_score(y_test,prediction)
svc.score(X_train,y_train)






#bbi=X[20].reshape(1, -1)

bbi='create a new folder'
review1 = re.sub('[^a-zA-Z]', ' ', bbi)
review1 = review1.lower()
review1 = review1.split()
ps = PorterStemmer()
review1 = [ps.stem(word) for word in review1 if not word in set(stopwords.words('english'))]
review1 = ' '.join(review1)
review1=[review1]
review1 = cv.fit_transform(review1).toarray()

mahmoud=svc.predict(review1)









