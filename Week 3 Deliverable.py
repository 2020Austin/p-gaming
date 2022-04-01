#extreme gradient boosting

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

league0 = '/Users/loan/league_dataset.csv'
df = pd.read_csv(league0)

arr = df.to_numpy()

#array slicing
all_data = arr[:, 1 : -1] #gets rid of index column and excludes label column
all_labels = arr[:, -1]  #assumes labels are in last column, hence -1

x=all_data
y=all_labels

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2)

model=XGBClassifier() 
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print(y_test)
print(y_pred)
print(accuracy_score(y_test, y_pred)*100)

#logistic regression

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

league0 = '/Users/loan/league_dataset.csv'
df = pd.read_csv(league0)

arr = df.to_numpy()

#array slicing
all_data = arr[:, 1 : -1] #gets rid of index column and excludes label column
all_labels = arr[:, -1]  #assumes labels are in last column, hence -1

x=all_data
y=all_labels

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2)

logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)
logisticRegr.predict(x_test[0].reshape(1,-1))
logisticRegr.predict(x_test[0:10])
predictions = logisticRegr.predict(x_test)
print(predictions)

score = logisticRegr.score(x_test, y_test)
print(score)
print(y_test)

print(logisticRegr.coef_)

#decision trees

import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

league0 = '/Users/loan/league_dataset.csv'
df = pd.read_csv(league0)

arr = df.to_numpy()

#array slicing
all_data = arr[:, 1 : -1] #gets rid of index column and excludes label column
all_labels = arr[:, -1]  #assumes labels are in last column, hence -1

x=all_data
y=all_labels

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2)

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(x_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(x_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print(y_train)
print(y_pred)

print(clf.feature_importances_)