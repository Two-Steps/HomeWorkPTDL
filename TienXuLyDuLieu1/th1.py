# Chuẩn hóa dữ liệu với Z-Score Scaling

# Công thức của nó là: z = (x – u) / s
# Trong đó: u là mean của dữ liệu huấn luyện, s là độ lệch chuẩn, 
# x là điểm dữ liệu cần chuẩn hóa, z là dữ liệu được chuẩn hóa

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Khởi tạo dữ liệu
# tạo các cột theo các phần phối khác nhau
df = pd.DataFrame({
    'beta': np.random.beta(5, 1, 1000) * 60,
    'exponential': np.random.exponential(10, 1000),
    'normal_p': np.random.normal(10, 2, 1000),
    'normal_l': np.random.normal(10, 10, 1000),
})

# thêm dữ liệu được tạo theo phân phối nhị thức
first_half = np.random.normal(20, 3, 500)
second_half = np.random.normal(-20, 3, 500)
bimodal = np.concatenate([first_half, second_half])
df['bimodal'] = bimodal

# print(df.head())

# trực quan hóa dữ liệu sinh ra 
sns.kdeplot(data=df)
# plt.show()
df.describe()

# Thêm 1 đặc trưng với giá trị lớn hơn nhiều
normal_big = np.random.normal(1000000, 10000, (1000, 1))
df['normal_big'] = normal_big
# sns.kdeplot(data=df)
# plt.show()

# Trực quan hóa bằng biểu dồ box plot
# df.boxplot()
# plt.show()

## 1. Chuẩn hóa với StandardScaler - Z-Score scaling

# khai báo đối tượng StanderdScaler
s_scaler = StandardScaler()
# chuẩn hóa dữ liệu trong df
df_s = s_scaler.fit_transform(df)
# lấy danh sách các cột
col_names = list(df.columns)
# chuyển về DataFrame, gán các cột của df cho dữ liệu đã chuẩn hóa
df_s = pd.DataFrame(df_s, columns=col_names)
print(df_s.head())

# biểu diễn dữ liệu đã được chuẩn hóa
# sns.kdeplot(data = df_s)
# plt.show()

# thống kê về dữ liệu được sinh ra
# print(df_s.describe())

# Trực quan hóa băng box plot
df_s.boxplot()
plt.show()

