# Chuẩn hóa dữ liệu với Min Max Scaling thông qua Scikit-Learn
# Công thức của nó là:
# X_std = (X – X.min(axis=0)) / (X.max(axis=0) – X.min(axis=0))
# X_scaled = X_std * (max – min) + min
# Trong đó:
# X là điểm dữ liệu cần chuẩn hóa, 
# X_scaled là dữ liệu được chuẩn hóa,
# X_std là tỉ lệ chuẩn hóa, 
# max và min là khoảng chuẩn hóa của giá trị.
# Cách chuẩn hóa này thường mang lại hiệu quả tốt hơn đối với 
# tác vụ hồi quy hơn so với các tác vụ phân lớp.
# ** nhược điểm: nhạy cảm với dữ liệu ngoại lai

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# 1. Khởi tạo dữ liệu 
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

print(df.head())

# 2. Trực quan hóa
# sns.kdeplot(data=df)
# plt.show()

# 3. Thống kê dữ liệu vừa sinh ra
print(df.describe())

# 4. Thêm 1 đặc trưng với giá trị lớn hơn rất nhiều
normal_big = np.random.normal(1000000, 10000, (1000, 1))
df['normal_big'] = normal_big
# sns.kdeplot(data = df)
# plt.show()

# 5. Trực quan hóa bằng biểu đồ box plot
# df.boxplot()
# plt.show()

# --------------- Chuẩn hóa với Min Max Scaling ------------------
# 1. Khai báo đối tượng MinMaxScaler
scaler = MinMaxScaler()
# 2. Chuẩn hóa dữ liệu trong df với MinMaxScaler
df_s = scaler.fit_transform(df)
# 3. Lấy danh sách các cột
col_names = list(df.columns)
# 4. Chuyển về DataFrame, gán các cột của df cho dữ liệu được chuẩn hóa
df_s = pd.DataFrame(df_s, columns=col_names)
# print(df_s.head())

# 5. Biểu diễn dữ liệu đã được chuẩn hóa
# sns.kdeplot(data=df_s)
# plt.show()

# 6. Trực quan hóa
# df_s.boxplot()
# plt.show()

# In các giá trị min của từng cột dữ liệu chưa chuẩn hóa
mins = [df[col].min() for col in df.columns]
print()
print('Min chưa chuẩn hóa: ',mins)
# In các giá trị min của từng cột dữ liệu đã chuẩn hóa
mins2 = [df_s[col].min() for col in df_s.columns]
print()
print('Min đã chuẩn hóa: ', mins2)
# In các giá trị max của từng cột dữ liệu chưa chuẩn hóa
maxs = [df[col].max() for col in df.columns]
print()
print('Max chưa chuẩn hóa: ',maxs)
# In các giá trị min của từng cột dữ liệu đã chuẩn hóa
maxs2 = [df_s[col].max() for col in df_s.columns]
print()
print('Max đã chuẩn hóa: ', maxs2)
