import pandas as pd
import numpy

fields = ['PassengerId', 'Sex']

df = pd.read_csv('dataset/train.csv', usecols=fields)
#print(df.values)

print(df.groupby(fields).groups.keys())