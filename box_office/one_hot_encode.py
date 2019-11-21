#one-hot encode data
import re
import pandas as pd
import numpy as np

path_to_train = 'resources/training_data.csv'
path_to_test = 'resources/test_data.csv'

data = pd.read_csv(path_to_train)

#replace genres with non numerical values
dict = {12:'a',14:'b',16:'c',18:'d',27:'e',28:'f',35:'g',36:'h',37:'i',53:'j',80:'k',99:'l',878:'m',9648:'n',10402:'o',10749:'p',10751:'q',10752:'r',10769:'s',10770:'t'}
#data.replace({"genres",dict})
data['genres'] = data['genres'].map(dict)
data = pd.get_dummies(data)

print(data.describe())

data.to_csv(r'resources/full_training_data.csv',index=False)