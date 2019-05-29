import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
import sklearn
import sys
import os
import random
import nltk
import requests # to send the data to the server
import json # to print the data or result to the terminal
import pickle ## to save the our trained data to the disk
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
#loading the dataset
dataset = pd.read_csv('Salary_Data.csv')
# slicing the dataset into the prediction and the features
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

# making the test and trianing dataset

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.27,random_state =0)

# fitting the data

model = LinearRegression()
model.fit(X_train,Y_train)

# prediction on the test dataset
y_pred   = model.predict(X_test)

# measuring the error (log mean squared error)

from sklearn.metrics import accuracy_score, mean_squared_error,mean_squared_log_error

# the results
print(mean_squared_log_error(Y_test,y_pred))
#print(mean_squared_log_error(Y_test,y_logic_pred))

#exporting the trained model
pickle.dump(model, open('model.pkl','wb'))
