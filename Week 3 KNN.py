from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "league_dataset.csv"
df = pd.read_csv(filename)

arr = df.to_numpy()
all_data = arr[:, : -1]
all_labels = arr[:, -1]
training_data, testing_data, training_labels, testing_labels = train_test_split(all_data, all_labels, test_size=0.1234)

blue_kills = training_data[:, [1]]
red_kills = training_data[:, [2]]
blue_assists = training_data[:, [3]]
red_assists = training_data[:, [4]]
blue_gold = training_data[:, [5]]
red_gold = training_data[:, [6]]
game_length = training_data[:, [7]]

def model_func_param(paramater, index): #Use this function if you want to enter a paramater.
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(paramater, training_labels)
    print("predicted:", model.predict(testing_data[:, [index]]))
    print("real:" , testing_labels)


def model_func(): # Use this function if you want to run with all paramaters.
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(training_data, training_labels)
    print("predicted:", model.predict(testing_data))
    print("real:" , testing_labels)



