def clean_data(path_to_csv,column_names,index):
    import pandas as pd
    import numpy as np
    #get training data
    csv_data = pd.read_csv(path_to_csv, index_col=index)   
    #to start with use the following fields, as a guess:
    #budget, genre, language, popularity, production company, release date
    #col_names = ["budget","genres","original_language","popularity","production_companies","release_date","revenue"]
    reduced_data = csv_data[column_names]
    #only use entries which don't contain null values
    complete_data = reduced_data.dropna()
    #remove entries where budget is zero
    #complete_data_2 = complete_data_1[complete_data_1.budget != 0]
    #print(complete_data_2.head)

    #training_output = complete_data_1[output]
    #training_data = complete_data_1.drop(output,axis=1)
    
    return complete_data;