import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

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



clf = GradientBoostingClassifier(n_estimators=100, learning_rate=2.0,
 max_depth=1, random_state=0).fit(x_train, y_train)
print(clf.score(x_test, y_test)*100, "%")
print(clf.feature_importances_) 