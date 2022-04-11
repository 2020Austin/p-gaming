from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "league_dataset2.csv"
df = pd.read_csv(filename)

arr = df.to_numpy()
all_data = arr[:,4 : -1]
all_labels = arr[:, -1]
all_labels = all_labels.astype('int')
training_data, testing_data, training_labels, testing_labels = train_test_split(all_data, all_labels, test_size=0.2, random_state=2)


def model_func_param(paramater, index): #Use this function if you want to enter a paramater.
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(paramater, training_labels)
    print("predicted:", model.predict(testing_data[:, [index]]))
    print("real:" , testing_labels)
    y_pred=model.predict(testing_data[:, [index]]) 
    print("Accuracy:",(metrics.accuracy_score(testing_labels, y_pred))*100, "%")


def model_func(): # Use this function if you want to run with all paramaters.
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(training_data, training_labels)
    print("predicted:", model.predict(testing_data))
    print("real:" , testing_labels)
    y_pred=model.predict(testing_data) 
    print("Accuracy:",(metrics.accuracy_score(testing_labels, y_pred))*100, "%")

model_func()