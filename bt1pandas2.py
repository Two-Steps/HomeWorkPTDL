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
df2 = df.groupby('Continent').sum()
df2.columns = ['Total']
print(df2)
df3 = df.groupby('Continent').mean()
df3.columns = ['AVG']
print(df3)

df4 = pd.concat([df2, df3], axis=1)
print(df4)