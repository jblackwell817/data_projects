#import the data
from clean_data import clean_data
path_to_csv = 'resources/train.csv'
col_names = ["budget","genres","original_language","popularity","production_companies","release_date","revenue"]
index = 'id'

clean_data = clean_data(path_to_csv,col_names,index)
complete_data = clean_data[clean_data.budget != 0]
training_data = complete_data.drop('revenue',axis=1)
training_output = complete_data['revenue']

#print(training_data.head)
#print(training_output.head)