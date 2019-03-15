import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dataset = pd.read_csv('data/dataset.csv', sep = ',', encoding='utf8')

##########################################

# adding headers to the dataset
dataset.columns = ["desc", "target"]
dataset.head()


###########################################


#label all targets with numbers
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
dataset_target = dataset["target"]
target = encoder.fit_transform(dataset_target)


#label all inputs with numbers
dataset_desc = dataset["desc"]
desc = encoder.fit_transform(dataset_desc)


##########################################


#adding new columns
dataset['target_num'] = target
dataset['dec_num'] = desc
dataset.head()


#########################################


X = dataset['dec_num'] #input
y = dataset['target_num'] #output

from sklearn.model_selection import train_test_split
X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


#########################################



#reshape X and y to become 2D array (because .fit accepts only 2D arrays)
y_test = y_test.values.reshape(-1,1)
y_train = y_train.values.reshape(-1,1)

x_test = x_test.values.reshape(-1,1)
X_train = X_train.values.reshape(-1,1)


########################################


#applying KNN model
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, np.ravel(y_train,order='C'))
y_pred = classifier.predict(x_test)


########################################



#view F1 score
print(classification_report(y_test, y_pred))

