import pandas as pd
records = pd.DataFrame()

# data analysis
records.describe()

# categorical analysis


stats_sex = records.groupby(by='sex').describe()
records.groupby(by='sex').agg({'game': 'mean'})


# imbalanced class analysis


# response - feature correlation
k = records.iloc[0]
records.append(k)

records.loc[0, 'chatting'] = 5