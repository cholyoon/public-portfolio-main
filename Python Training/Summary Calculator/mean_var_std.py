import numpy as np

def calculate(x):
    #throw exception with ValueError length of array < 9
    if len(x) < 9:
        raise ValueError('List must contain nine numbers.')


    #reshape to 3,3
    arr = np.array(x)
    arr_reshaped = arr.reshape(3,3)

    #initiating dict
    calculations = {}

    #calculate stats [column, row, flatten]
    mean_list = [np.mean(arr_reshaped,axis=0).tolist(), np.mean(arr_reshaped,axis=1).tolist(),arr_reshaped.mean()]
    var_list = [np.var(arr_reshaped,axis=0).tolist(), np.var(arr_reshaped,axis=1).tolist(),arr_reshaped.var()]
    std_list = [np.std(arr_reshaped,axis=0).tolist(), np.std(arr_reshaped,axis=1).tolist(),arr_reshaped.std()]
    max_list = [np.max(arr_reshaped,axis=0).tolist(), np.max(arr_reshaped,axis=1).tolist(),arr_reshaped.max()]
    min_list = [np.min(arr_reshaped,axis=0).tolist(), np.min(arr_reshaped,axis=1).tolist(),arr_reshaped.min()]
    sum_list = [np.sum(arr_reshaped,axis=0).tolist(), np.sum(arr_reshaped,axis=1).tolist(),arr_reshaped.sum()]
    key_list = ['mean','variance','standard deviation','max','min','sum']
    
    #list for key and value pair 
    #using ZIP to create dic for return value
    value_list = [mean_list,var_list,std_list,max_list,min_list,sum_list]
    calculations = {k:v for k,v in zip(key_list,value_list)}

    return calculations