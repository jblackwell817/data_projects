#random forest for regression on continuous variables
import sys
import pandas as pd
import numpy as np
from random_forest_regressor import random_forest_regressor

#import the training data
path_to_data = 'resources/full_training_data.csv'
data = pd.read_csv(path_to_data)
feature_list = list(data.columns)
Xtrain = np.array(data)
#print(feature_list)
print(Xtrain.shape)

#import the labels
path_to_labels = 'resources/training_revenues.csv'
labels = pd.read_csv(path_to_labels)
ytrain = np.array(labels)
print(ytrain.shape)

#import the test data
path_to_test_data = 'resources/full_test_data.csv'
Xtest = pd.read_csv(path_to_test_data)

#create baseline

predicted_revenue, best_score = random_forest_regressor(Xtrain,Xtest,ytrain)

print(predicted_revenue)
np.savetxt('resources/predicted_revenues.csv',predicted_revenue,delimiter=',')
#predicted_revenue.to_csv(r'resources/predicted_revenues.csv',index=False)