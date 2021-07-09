import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
df = pd.DataFrame(data['Primary Fur Color'].value_counts())
df.reset_index(level=0, inplace=True)
df = df.rename(columns = {'index':'color', 'Primary Fur Color': 'count'})

df.to_csv('fur_color_count.csv')
