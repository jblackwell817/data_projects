def clean_data(path_to_csv,column_names,index):
    import pandas as pd
    import numpy as np
    #get training data
    csv_data = pd.read_csv(path_to_csv, index_col=index)   
    #reduce this dataframe to only the chosen columns
    reduced_data = csv_data[column_names]
    #only use entries which don't contain null values
    #complete_data = reduced_data.dropna()
        
    return reduced_data;