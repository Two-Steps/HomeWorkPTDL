# Vẽ biểu đồ kết hợp – GDP list
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('GDPlist.csv', encoding='latin1')
df['Country'] = df['Country'].str.strip()
# print(df.head(10))

# 1.Biểu đồ để hiển thị giá trị cụ thể và so sánh GDP các nước Vietnam,
# Indonesia, Cambodia, Thailand và Malaysia.
list_name = ['Vietnam','Indonesia', 'Cambodia', 'Thailand', 'Malaysia']
# list_value_gdp = df[df['Country'] == 'Vietnam']['GDP (millions of US$)'].values[0]
list_value_gdp = []
for i in list_name:
    v = df[df['Country'] == i]['GDP (millions of US$)'].values[0]
    list_value_gdp.append(v)
# 2.Biểu đồ để đánh giá tỉ lệ đóng góp GDP của các nước trên tổng số GDP 
# của 5 nước Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.
total_gdp = df['GDP (millions of US$)'].sum()
list_value_percent = []
for i in list_value_gdp:
    p = round(((i/total_gdp) * 100), 2)
    list_value_percent.append(p)
data1 = pd.DataFrame({'Country': list_name, 'GDP': list_value_gdp, 'GDP_percent': list_value_percent})
data1.plot(kind='bar', secondary_y='GDP_percent', rot=0, xlabel='Country', ylabel='GDP')
plt.show()
