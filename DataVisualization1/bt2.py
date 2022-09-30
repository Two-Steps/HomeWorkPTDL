# Phân tích bộ dữ liệu HousePrice _ Đống Đa
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('house_price_dống-da.xlsx')
# print(df.head(10))

#Vẽ biểu đồ phân tích mối liên hệ giữa diện tích với giá nhà, giữa số phòng
#  ngủ với giá nhà, giữa số toilet với giá nhà.
# ==> vẽ 1 biểu đồ đường với giá nhà là trục y, giá trị còn lại là x

# loại bỏ hết dòng k có giá
df1 = df[['price', 'bedroom', 'toilet', 'area']]
data = df1.dropna(subset=['price', 'area'])
# lấp đầy các giá trị trống của số phòng ngủ cũng như số toilet bằng giá trị trung bình
bed_avg = data['bedroom'].mean().__ceil__()
toi_avg = data['toilet'].mean().__ceil__()
data = data.fillna(value={'bedroom': bed_avg, 'toilet': toi_avg})
# print(data.head(10))
# chưa loại bỏ ngoại lai @_@
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
data = data[~((data < (Q1 - 1.5*IQR)) | (data > (Q3 + 1.5*IQR))).any(axis=1)]
# print(data.head(20))
# plt.plot(
#     data['area'].values,
#     data['price'].values,
# )
# plt.xlabel('Diện tích')
# plt.ylabel('Giá')
# plt.show()

# plt.plot(
#     data['bedroom'].values,
#     data['price'].values,
# )
# plt.xlabel('Phòng ngủ')
# plt.ylabel('Giá')
# plt.show()

# plt.plot(
#     data['toilet'].values,
#     data['price'].values,
# )
# plt.xlabel('Phòng vệ sinh')
# plt.ylabel('Giá')
# plt.show()

#  Vẽ biểu đồ so sánh giá nhà trung bình trên 1 m2 giữa các hình thức nhà 
# (type_of_land).
df2 = df[['price', 'type_of_land', 'area']]
df2['type_of_land'] = df2['type_of_land'].str.strip()
data2 = df2.dropna()
data2 = data2.replace({'area' : {0: data2['area'].mean()}})
data2['gia/m2'] = data2['price'] / data2['area']
data22 = data2.groupby('type_of_land')['gia/m2'].mean()
# plt.bar(
#     data22.index,
#     data22.values
# )
# plt.xlabel('Các loại nhà đất')
# plt.ylabel('Giá/m2')
# plt.show()

data23 = df2.dropna()
data23 = data23.replace({'area' : {0: data23['area'].mean()}})
d = data23['type_of_land'].value_counts()
# plt.pie(
#     d.values,
#     labels = d.index,
#     autopct='%.2f%%'
# )
# plt.title('Tỉ lệ % bài đăng (bản ghi) giữa các hình thức nhà')
# plt.show()

#Vẽ biểu đồ thể hiện sự thay đổi giá nhà trung bình trên 1m2 theo số lượng phòng ngủ.
df3 = df[['price', 'bedroom', 'area']]
data3 = df3.dropna()
data3 = data3.replace({'area' : {0: data3['area'].mean()}})
data3['gia/m2'] = data3['price'] / data3['area']
# print(data3.head())
plt.plot(
    data3['bedroom'],
    data3['gia/m2']
)
plt.show()





