# Trực quan hóa cơ bản dữ liệu FoodPrice_in_Turkey.csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

### => dữ liệu cần phải tiền xử lý đã nhé :3

# Chọn mục tiêu
# -1.Vẽ biểu đồ cột so sánh giá gạo (Rice-Retail) tháng 12 năm 2019 của Ankara,
# Istanbul, Izmir và National Average.
# -2.Vẽ biểu đồ đường phân tích xu hướng giá gạo (Rice-Retail) trung bình cả 
# nước (National Average) trong năm 2019 tại Thổ Nhĩ Kì.
# -3.Vẽ biểu đồ Scatter phân tích mối liên quan giữa giá gạo và giá gas 
# trung bình quốc gia (National Average) tại Thổ Nhĩ Kì.

df = pd.read_csv('FoodPrice_in_Turkey.csv')
print(df.info())
print(df.head(10))

# 1. Chọn dữ liệu cần thiết cho mục tiêu 1
# data1 = df[(df['Year'] == 2019) & (df['Month'] == 12) 
#         & (df['ProductName'] == 'Rice - Retail')]
# data1 = data1.replace({'Rice - Retail':'Rice'})
# print(data1)
# plt.bar(
#     data1['Place'],
#     data1['Price'],
#     width=0.5,       # chiều rộng cột
#     color = ['Red', 'Green', 'Blue', 'Black']  # màu sắc các cột

# )
# plt.title('Giá gạo tháng 12/2019', fontsize = 14)
# plt.xlabel('Địa điểm', fontsize = 12)
# plt.ylabel('Giá bán', fontsize = 12)
# plt.show()

# 2. Chọn dữ liệu cho mục tiêu 2
# data2 = df[(df['Year'] == 2019)&(df['Place'] == 'National Average')
#         &(df['ProductName'] == 'Rice - Retail')]
# print(data2.shape)
# plt.plot(
#     data2['Month'],
#     data2['Price'],
#     linestyle = '-',
#     marker = 'o',
#     color = 'k',
#     markerfacecolor = 'red',
#     markeredgecolor = 'blue',
#     markeredgewidth = 2
# )
# plt.title('Giá gạo các tháng trong năm 2019', fontsize = 14)
# plt.xlabel('Tháng')
# plt.ylabel('Giá gạo')
# plt.show()

# 3. Chọn dữ liệu cho mục tiêu 3
data_rice = df[(df['Place'] == 'National Average')
            &(df['ProductName'] == 'Rice - Retail')
            &(df['Year'] == 2019)]
data_gas = df[(df['Place'] == 'National Average')
            &(df['ProductName'] == 'Fuel (gas) - Retail')
            &(df['Year'] == 2019)]
# print(data_gas)
# print(data_rice)

plt.scatter(
    data_gas['Price'],
    data_rice['Price']
)
plt.title('Tương quan giá gạo & ga 2019', fontsize = 14)
plt.xlabel('Giá Gas', fontsize = 12)
plt.ylabel('Giá gạo', fontsize = 12)
plt.show()

