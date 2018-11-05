import pandas as pd
import numpy as np

size = 100
num_dur = 7
temp_durations = np.random.rand(size, num_dur)
temp_total = np.sum(temp_durations, axis=1)
percentages = pd.DataFrame(temp_durations, columns=['chatting', 'game', 'social_media', 'shopping', 'video', 'music', 'others'])
percentages['total'] = temp_total

percentages['chatting'] = percentages['chatting'] / percentages['total']
percentages['game'] = percentages['game'] / percentages['total']
percentages['social_media'] = percentages['social_media'] / percentages['total']
percentages['shopping'] = percentages['shopping'] / percentages['total']
percentages['video'] = percentages['video'] / percentages['total']
percentages['music'] = percentages['music'] / percentages['total']
percentages['others'] = percentages['others'] / percentages['total']
percentages['total'] = percentages['total'] / percentages['total']

durations = percentages
durations['total'] = np.random.randint(30, 360, size = size)
durations['chatting'] = durations['chatting'] * durations['total']
durations['game'] = durations['game'] * durations['total']
durations['social_media'] = durations['social_media'] * durations['total']
durations['shopping'] = durations['shopping'] * durations['total']
durations['video'] = durations['video'] * durations['total']
durations['music'] = durations['music'] * durations['total']
durations['others'] = durations['others'] * durations['total']


records = durations
records['exam_type'] = np.random.randint(3, size=size)
records['school_type'] = np.random.randint(3, size=size)
records['sex'] = np.random.randint(2, size=size)
records['success'] = np.random.randint(low=30, high=100, size=size)
records['age'] = np.random.randint(low=17, high=19, size=size)

# generate some missing values
temp = np.random.randint(low=0, high=99, size=10)
records.loc[temp, 'school_type'] = "?"
