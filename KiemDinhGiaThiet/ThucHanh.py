import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, ttest_1samp

# Kiểm định thống kê

# Kiểm ttest_independence

df = pd.read_csv('GDPlist.csv', encoding='latin1')
# print(df.head())
t1 = df[df['Continent'] == 'Asia']
t2 = df[df['Continent'] == 'Europe']

data1 = t1['GDP (millions of US$)'].values.tolist()
data2 = t2['GDP (millions of US$)'].values.tolist()

r = ttest_ind(data1, data2, equal_var= False)
print(r)

# Kiểm định ttest_samp
print(ttest_1samp(data1, popmean= 18181))
print(ttest_1samp(data1, popmean= 18181, alternative='less'))
print(ttest_1samp(data1, popmean= 18181, alternative='greater'))