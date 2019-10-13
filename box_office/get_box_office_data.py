#import the data
from clean_data import clean_data
import re
import pandas as pd
import numpy as np
path_to_csv = 'resources/train.csv'
#to start with use the following fields, as a guess:
#budget, genre, language, popularity, production company, release date
col_names = ["budget","genres","original_language","popularity","production_companies","release_date","revenue"]
index = 'id'

#get the clean data from the csv
clean_data = clean_data(path_to_csv,col_names,index)
#remove entries where budget is zero
complete_data = clean_data[clean_data.budget != 0]

training_data = complete_data.drop('revenue',axis=1)
training_output = complete_data['revenue']

#print(training_data.head)
#print(training_output.head)

#extract the genre using regex
row_count = training_data.shape[0]
zeros = np.zeros(shape=(row_count,1))
training_data['genre_id'] = zeros
training_data['prod_com_id'] = zeros
#get the id of the genre. ids are either two or five digit numbers, e.g. 12 =adventure, 10749 = romance
#regex = re.compile(r'\d\d|\d\d\d\d\d')
regex = re.compile(r'\d+')

#print(training_data.head)

for i in range(row_count):
    #print(i)
    gen_id = regex.search(training_data['genres'].iloc[i])
    prod_id = regex.search(training_data['production_companies'].iloc[i])
    training_data['genre_id'].iloc[i] = gen_id.group()
    training_data['prod_com_id'].iloc[i] = prod_id.group()
    #print(training_data.head)

new_training_data =training_data.drop(['genres','production_companies'],axis=1)
export_training_data = new_training_data.to_csv(r'resources/reduced_training_data.csv',index=False)
export_training_results = training_output.to_csv(r'resources/training_revenue.csv',index=False)
#print(training_data.head)