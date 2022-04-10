import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('/Users/loan/leagueDiamond1.csv')

print(df)

arr = df.to_numpy()

all_data = arr[:, 1 : -1] 
all_labels = arr[:, -1]

x=all_data
y=all_labels

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2)

clf = DecisionTreeClassifier()

clf = clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

# Xin Yi

df = pd.read_csv('/Users/loan/leagueDiamond1.csv')


arr = df.to_numpy()

print(arr)

arr = arr[:,2 :]

#arr = arr.astype(float)

#array slicing
all_data = arr[:, 0 : -1] #gets rid of index column and excludes label column
all_labels = arr[:, -1]  #assumes labels are in last column, hence -1

training_data, testing_data, training_labels, testing_labels = train_test_split(all_data, all_labels, test_size=0.2)

my_tree = DecisionTreeClassifier()
my_tree.fit(training_data, training_labels)
my_tree.score(testing_data, testing_labels)