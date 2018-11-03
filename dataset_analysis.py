import pandas as pd

df = pd.read_csv('/Users/mob/PycharmProjects/cikoai/dataset/reprocessed.hungarian.data.txt', delimiter=' ', header=None)
df = df.replace(-9,'?')


# imbalanced class analysis


# response - feature correlation
