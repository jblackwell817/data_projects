#import the data
import re
import pandas as pd
import numpy as np

path_to_train = 'resources/train.csv'
path_to_test = 'resources/test.csv'
#to start with use the following fields, as a guess:
#budget, genre, language, popularity, production company, release date
col_names_train = ["budget","genres","original_language","popularity","release_date","revenue"]
col_names_test = ["budget","genres","original_language","popularity","release_date"]
index = 'id'

#get the data from csvs and reduce to only columns interested in
csv = pd.read_csv(path_to_test, index_col=index)
reduced_data = csv[col_names_test]

#use average budget where budget = 0
budgets = reduced_data["budget"]
budgets=budgets.mask(budgets==0).fillna(budgets.mean())

#if date doesn't exist, replace with 01/01/2000 (only one entry doesn't have date)
dates = reduced_data["release_date"]
for i in range(dates.size):
    y = dates.iloc[i]
    if pd.isnull(y):
        dates.iloc[i] = '01/01/2000'
dates = pd.to_datetime(dates)

for i in range(dates.size):
    dates.iloc[i] = dates.iloc[i].year

#use most common genre where genre not specified
genres = reduced_data["genres"]

mode = genres.mode()
mode_value = mode.iloc[0]

for i in range(genres.size):
    x = genres.iloc[i]
    if pd.isnull(x):
        genres.iloc[i] = mode_value

#use regex to get genre id
regex = re.compile(r'\d+')

for i in range(genres.size):
    gen_id = regex.search(genres.iloc[i]).group()
    genres.iloc[i] = gen_id

#replace original dataframe with cleaned values
reduced_data["budget"] = budgets
reduced_data["genres"] = genres
reduced_data["release_date"] = dates

reduced_data.to_csv(r'resources/complete_test_data.csv',index=False)