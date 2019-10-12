import pandas as pd
import numpy as np

#get training data
training_data = pd.read_csv('resources/train.csv', index_col="id")
#to start with use the following fields, as a guess:
#budget, genre, language, popularity, production company, release date
col_names = ["budget","genres","original_language","popularity","production_companies","release_date","revenue"]
reduced_data = training_data[col_names]
#only use entries which don't contain null values
complete_data = reduced_data.dropna()
print(complete_data.head)

