import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_excel('Dry_Bean_Dataset.xlsx')
dataset.head(5)

X = dataset.iloc[:, [0,1,2,3,4]].values
y = dataset.iloc[:, -1].values

#label encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

#preprocessing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#modelling using XGBoost
from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

#making confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
#printing result to terminal
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
#print(cm)
hasil = {"hasil" : y_pred}
print(hasil)
accuracy_score(y_test, y_pred)

# Saving model to disk
pickle.dump(classifier, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

