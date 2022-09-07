# Phân tích với bộ dữ liệu GDP List
import pandas as pd
import numpy as np

df = pd.read_csv('GDPlist.csv', encoding='latin1')
# print(df)
# ['Country', 'Continent', 'GDP (millions of US$)']
df.rename(columns={'GDP (millions of US$)':'GDP'}, inplace=True)

# print('Số dòng: ' + str(df.shape[0]))
# print('Số cột: ' + str(df.shape[1]))
# print(df.info())

# Giá trị GDP max
# gdp_max = df['GDP'].max()
# print('GDP max: ', gdp_max)
# # Giá trị GDP min
# gdp_min = df['GDP'].min()
# print('GDP min: ', gdp_min)

gdp_mean = df['GDP'].mean()
gdp_mode = df['GDP'].mode()
gdp_median = df['GDP'].median()

# if gdp_mode > gdp_median and gdp_median > gdp_mean:
#     print('Phân bố lệch trái')
# if gdp_mode < gdp_median and gdp_median < gdp_mean:
#     print('Phân bố lệch phải')

# - Châu lục xuất hiện nhiều nhất
df1 = df.groupby('Continent')['Country'].count().sort_values(ascending=False)
# print(df1)

# tổng gdp, trung bình gdp mỗi châu lục
df2 = pd.DataFrame()
df2['Continent'] = df.groupby('Continent').sum().index
df2['Total'] = df.groupby('Continent').sum().loc[:, :]
print(df2)