# Trực quan hóa cơ bản dữ liệu GDP list
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('GDPlist.csv', encoding='latin1')
# print(df.head(10))
# 1.So sánh GDP các nước ở South America
data1 = df[df['Continent'] == 'South America']
# print(data1)
# plt.bar(
#     data1['Country'],
#     data1['GDP (millions of US$)'],
#     # label = []
# )
# plt.title('GDP of Sounth America', fontsize = 14)
# plt.xlabel('Country', fontsize = 12)
# plt.ylabel('GDP (Millions USD)')
# plt.show()

# 2.Đánh giá tỉ lệ đóng góp GDP của Việt Nam trên tổng số GDP của 5 nước 
# Đông Nam Á là Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.
df['Country'] = df['Country'].str.slice(start=1)
data2 = df[
    (df['Country'] == 'Vietnam') |
    (df['Country'] == 'Indonesia') |
    (df['Country'] == 'Cambodia') |
    (df['Country'] == 'Thailand') |
    (df['Country'] == 'Malaysia') 
]
# print(data2)
labels = ['Vietnam', 'Indonesia', 'Cambodia', 'Thailand', 'Malaysia']
d = data2[data2['Country'] == 'Vietnam']['GDP (millions of US$)'].values[0]
list_values = []
for i in labels:
    d = data2[data2['Country'] == i]['GDP (millions of US$)'].values[0]
    list_values.append(d)
plt.pie(list_values, labels=labels, autopct='%.2f%%')
plt.title('Tỉ lệ đóng góp GDP các nước ĐNÁ')
plt.show()