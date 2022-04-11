from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "league_dataset2.csv"
df = pd.read_csv(filename)

arr = df.to_numpy()
all_data = arr[:,3 : -1]
all_labels = arr[:, -1]
all_labels = all_labels.astype('int')
training_data, testing_data, training_labels, testing_labels = train_test_split(all_data, all_labels, test_size=0.2, random_state=2)

knn = KNeighborsClassifier()
dtc = DecisionTreeClassifier()
rfc = RandomForestClassifier()
gbc = GradientBoostingClassifier()


from sklearn.model_selection import GridSearchCV
k_range = list(range(1, 31))
param_grid = dict(n_neighbors=k_range)
param_grid2 = dict(max_depth=k_range)
param_grid3 = dict(learning_rate=k_range)
# defining parameter range
grid_knn = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy', return_train_score=False,verbose=1)
grid_tree = GridSearchCV(dtc, param_grid2, cv=10, scoring='accuracy', return_train_score=False,verbose=1)
grid_forest = GridSearchCV(rfc, param_grid2, cv=10, scoring='accuracy', return_train_score=False,verbose=1)
grid_gradient = GridSearchCV(gbc, param_grid3, cv=10, scoring='accuracy', return_train_score=False,verbose=1)

# fitting the model for grid search
grid_search=grid_knn.fit(training_data, training_labels)
grid_search2=grid_tree.fit(training_data, training_labels)
grid_search3=grid_forest.fit(training_data, training_labels)
grid_search4=grid_gradient.fit(training_data, training_labels)

print(grid_search.best_params_)
accuracy = grid_search.best_score_ *100
print("Accuracy for our training dataset with tuning is : {:.2f}%".format(accuracy) )


print(grid_search2.best_params_)
accuracy = grid_search2.best_score_ *100
print("Accuracy for our training dataset with tuning is : {:.2f}%".format(accuracy) )

print(grid_search3.best_params_)
accuracy = grid_search3.best_score_ *100
print("Accuracy for our training dataset with tuning is : {:.2f}%".format(accuracy) )

print(grid_search4.best_params_)
accuracy = grid_search4.best_score_ *100
print("Accuracy for our training dataset with tuning is : {:.2f}%".format(accuracy) )