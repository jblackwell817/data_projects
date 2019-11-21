#use only continuous variables in predictor
import pandas as pd
import numpy as np
#load the reduced dataset
#path_to_training_data = 'resources/reduced_training_data.csv'
#training_data = pd.read_csv(path_to_training_data)

path_to_test_data = 'resources/reduced_test_data.csv'
test_data = pd.read_csv(path_to_test_data)

#print(data.head)

#row_count_training = training_data.shape[0]
#training_zeros = np.zeros(shape=(row_count_training,1))
#training_data['year'] = training_zeros
#training_data['release_date'] = pd.to_datetime(training_data['release_date'])

row_count_test = test_data.shape[0]
test_zeros = np.zeros(shape=(row_count_test,1))
test_data['year'] = test_zeros
test_data['release_date'] = pd.to_datetime(test_data['release_date'])

#convert datetime to years

#for i in range(row_count_training):
#    training_data['year'].iloc[i] = training_data['release_date'].iloc[i].year

for i in range(row_count_test):
    test_data['year'].iloc[i] = test_data['release_date'].iloc[i].year

#print(data.head)

continuous_variables = ['budget','popularity','year']
#continuous_training_data = training_data[continuous_variables]
#export_continuous_training_data = continuous_training_data.to_csv(r'resources/continuous_training_data.csv',index=False)
#print(continuous_data.head)

continuous_test_data = test_data[continuous_variables]
export_continuous_test_data = continuous_test_data.to_csv(r'resources/continuous_test_data.csv',index=False)
print('done')
#convert datetimes to years