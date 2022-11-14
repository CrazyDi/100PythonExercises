import pandas as pd

df = pd.read_csv('countries_by_area.txt')

df['dense'] = df['population_2013'] / df['area_sqkm']

print(list(df.sort_values(by=['dense'], ascending=False).head(5)['country']))

