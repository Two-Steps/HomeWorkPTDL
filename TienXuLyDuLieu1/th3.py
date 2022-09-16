# Chuẩn hóa dữ liệu với Robust Scaling
# Thư viện Scikit-learn hỗ trợ chúng ta chuẩn hóa dữ liệu bằng phương pháp 
# Min-Max Scaling thông qua hàm RobustScaler trong module Preprocessing.
# Hàm này sẽ chuyển đổi các đặc trưng bằng cách scale mỗi đặc trưng sử 
# dụng thống kê, loại bỏ ngoại lai.
# Mặc định, RobustScaler trong scikit-learn cũng sẽ căn giữa và scale về khoảng tứ phần tư tương ứng.

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler

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
# print(df.describe())

# 4. Thêm 1 đặc trưng với giá trị lớn hơn rất nhiều
normal_big = np.random.normal(1000000, 10000, (1000, 1))
df['normal_big'] = normal_big
# sns.kdeplot(data = df)
# plt.show()

# 5. Trực quan hóa bằng biểu đồ box plot
# df.boxplot()
# plt.show()

# ----------------- Chuẩn hóa với Robust Scaling -----------------
# 1. Khai báo đối tượng RobustScaler
scaler = RobustScaler()
# 2. Chuẩn hóa dữ liệu trong df với RobustScaler
df_s = scaler.fit_transform(df)
# 3. Lấy danh sách các cột
col_names = list(df.columns)
# 4. Chuyển về DataFrame, gác các cột của df đã chuẩn hóa
df_s = pd.DataFrame(df_s, columns=col_names)
print(df_s.head())
# 5. Biểu diễn dữ liệu đã được chuẩn hóa
# sns.kdeplot(data=df_s)
# plt.show()
# 6. Lấy giá trị max ở mỗi cột
maxs = [df_s[col].max() for col in df_s.columns]
# 7. Lấy giá trị min ở mỗi cột
mins = [df_s[col].min() for col in df_s.columns]
# 8. # giá trị trung vị của các đặc trưng của tập dữ liệu gốc
print(scaler.center_)
print(maxs)
print(mins)