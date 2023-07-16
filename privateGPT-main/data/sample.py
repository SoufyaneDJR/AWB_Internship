import random
import string
import pandas as pd 
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst
sample = pd.read_csv("data\\sample.csv")

columns = list(sample.columns)
reverse = Reverse(columns)

for i, column in enumerate(reverse) : 
    print(i, column)
    sample[reverse[i]] = sample[reverse[i+1]]
    if column == "Pull Request ID" : 
        break


sample['Pull Request ID'] = [''.join(random.choices(string.ascii_letters + string.digits, k=8)) for _ in range(len(sample))]
del sample[sample.columns[0]]
sample.to_csv("data\\sample_shifted.csv")
