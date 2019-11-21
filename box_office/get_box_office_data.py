#import the data
from clean_data import clean_data
import re
import pandas as pd
import numpy as np
path_to_train = 'resources/train.csv'
path_to_test = 'resources/test.csv'
#to start with use the following fields, as a guess:
#budget, genre, language, popularity, production company, release date
col_names_train = ["budget","genres","original_language","popularity","production_companies","release_date","revenue"]
col_names_test = ["budget","genres","original_language","popularity","production_companies","release_date"]
index = 'id'

#get the clean data from the csv
clean_training_data = clean_data(path_to_train,col_names_train,index)
clean_test_data = clean_data(path_to_test,col_names_test,index)
#remove entries where budget is zero
complete_training_data = clean_training_data[clean_training_data.budget != 0]
test_data = clean_test_data[clean_test_data.budget != 0]
#split data from labels
training_data = complete_training_data.drop('revenue',axis=1)
training_output = complete_training_data['revenue']

#print(training_data.head)
#print(training_output.head)

#extract the genre using regex
row_count_train = training_data.shape[0]
zeros_train = np.zeros(shape=(row_count_train,1))
training_data['genre_id'] = zeros_train
training_data['prod_com_id'] = zeros_train

row_count_test = test_data.shape[0]
zeros_test = np.zeros(shape=(row_count_test,1))
test_data['genre_id'] = zeros_test
test_data['prod_com_id'] = zeros_test

#get the id of the genre. ids are either two or five digit numbers, e.g. 12 =adventure, 10749 = romance
regex = re.compile(r'\d+')


for i in range(row_count_train):
    #print(i)
    gen_id = regex.search(training_data['genres'].iloc[i])
    prod_id = regex.search(training_data['production_companies'].iloc[i])
    training_data['genre_id'].iloc[i] = gen_id.group()
    training_data['prod_com_id'].iloc[i] = prod_id.group()

for i in range(row_count_test):
    #print(i)
    gen_id = regex.search(test_data['genres'].iloc[i])
    prod_id = regex.search(test_data['production_companies'].iloc[i])
    test_data['genre_id'].iloc[i] = gen_id.group()
    test_data['prod_com_id'].iloc[i] = prod_id.group()


new_training_data =training_data.drop(['genres','production_companies'],axis=1)
export_training_data = new_training_data.to_csv(r'resources/reduced_training_data.csv',index=False)
export_training_results = training_output.to_csv(r'resources/training_revenue.csv',index=False)
#print(training_data.head)

new_test_data =test_data.drop(['genres','production_companies'],axis=1)
export_test_data = new_test_data.to_csv(r'resources/reduced_test_data.csv',index=False)