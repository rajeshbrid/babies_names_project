# %load q01_create_dict/build.py
import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

'write your solution here'

def q01_create_dict(data):
    dictionary = {'Name':data['Name'],
                 'Count':data['Count']}
    # print (dictionary)
    return dictionary

# q01_create_dict(data)



