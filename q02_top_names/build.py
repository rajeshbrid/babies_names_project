# %load q02_top_names/build.py
import pandas as pd
from collections import Counter
from greyatomlib.babies_names_project.q01_create_dict.build import q01_create_dict

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

'write your solution here'

def q02_top_names(data):
    dict_1 = q01_create_dict(data)
    dict_2 = Counter(dict_1).most_common(25)
    # print (dict_2, dict_1)
    return dict_2, dict_1

# q02_top_names(data)




