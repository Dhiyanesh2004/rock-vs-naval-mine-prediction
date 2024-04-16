# -*- coding: utf-8 -*-
"""ProjectDRS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jsFwOc0KkZq913cDBIWn_htxHSw_10I-
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load dataset to pandas dataframe
sonar_data = pd.read_csv('/content/Copy of sonar data.csv', header=None)

# Separating data and labels
X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

# Splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

# Standardizing the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training the Logistic Regression model
model = LogisticRegression()
model.fit(X_train_scaled, Y_train)

# Accuracy on training data
train_predictions = model.predict(X_train_scaled)
training_accuracy = accuracy_score(train_predictions, Y_train)
print('Accuracy on training data:', training_accuracy)

# Accuracy on test data
test_predictions = model.predict(X_test_scaled)
test_accuracy = accuracy_score(test_predictions, Y_test)
print('Accuracy on test data:', test_accuracy)

# Now let's make a prediction using your input data
input_data = [0.0453,0.0523,0.0843,0.0689,0.1183,0.2583,0.2156,0.3481,0.3337,0.2872,0.4918,0.6552,0.6919,0.7797,0.7464,0.9444,1.0000,0.8874,0.8024,0.7818,0.5212,0.4052,0.3957,0.3914,0.3250,0.3200,0.3271,0.2767,0.4423,0.2028,0.3788,0.2947,0.1984,0.2341,0.1306,0.4182,0.3835,0.1057,0.1840,0.1970,0.1674,0.0583,0.1401,0.1628,0.0621,0.0203,0.0530,0.0742,0.0409,0.0061,0.0125,0.0084,0.0089,0.0048,0.0094,0.0191,0.0140,0.0049,0.0052,0.0044]

# Reshape the input data and scale it
input_data_scaled = scaler.transform([input_data])

# Make prediction
prediction = model.predict(input_data_scaled)
print('Prediction:', prediction)

if (prediction[0]=='R'):
  print('The object is a rock')
else:
  print('The object is a mine')