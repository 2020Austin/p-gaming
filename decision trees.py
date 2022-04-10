import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('/Users/loan/leagueDiamond1.csv')

df.head()

arr = df.to_numpy()

all_data = arr[:,3:-1] #gets rid of index column and excludes label column
all_labels = arr[:,-1]  #assumes labels are in last column, hence -1

x=all_data
y=all_labels

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2)

clf = DecisionTreeClassifier()

clf = clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)