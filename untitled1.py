# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:46:47 2019

@author: NR
"""
#importing the libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset using pandas
dataset = pd.read_csv('phishing.txt')

#separating the features and label
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,30].values

#Creating the traing set 
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.3 , random_state = 0)

'''# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)  ''''

#creating the model using KNN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
classifier.score(X_train,y_train)
classifier.score(X_test,y_test)