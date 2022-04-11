from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
import pandas as pd

league0 = 'league_dataset2.csv'
df = pd.read_csv(league0)

arr = df.to_numpy()

#array slicing
all_data = arr[:, 4 : -1] #gets rid of index column and excludes label column
all_labels = arr[:, -1]  #assumes labels are in last column, hence -1

x=all_data
y=all_labels
y=y.astype('int')

x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state = 2)

clf = RandomForestClassifier(max_depth=7, random_state=0)
clf.fit(x_train, y_train)

print(clf.predict(x_test))
y_pred=clf.predict(x_test) 
print("Accuracy:",(metrics.accuracy_score(y_test, y_pred))*100, "%")
print(clf.feature_importances_)