# Phân tích dữ liệu Credit_scoring
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

df = pd.read_csv('TienXuLuDuLieu2\Credit_Scoring.csv')
print(df.info())
print(df.describe())

# Kiểm tra dữ liệu khuyết thiếu
# print(df.isna())

# Thay thế giá trị khuyết thiếu bằng giá trị nội suy theo các cột
# df2 = df
# df2 = df2.interpolate(axis=1)
# print(df2.info())

# Thay thế giá trị khuyết thiếu bằng giá trị 0
df = df.fillna(0)
# print(df.info())

# Vẽ biểu đồ boxplot, biểu đồ phân bố dữ liệu cho các cột
# sns.boxplot(data=df)
# plt.show()

# Loại bỏ ngoại lai
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
# xác định phần tử không phải ngoại lai
df6 = df
df6 = df[~((df < (Q1 - 1.5*IQR)) | (df > (Q3 + 1.5*IQR))).any(axis=1)]
# print(df6.info())

# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng phần tử bằng nhau 
# và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng giữ liệu của mỗi nhóm
col_names = list(df.columns)
#Chia dữ liệu ở các cột age và MonthlyIncome thành 5 nhóm theo các khoảng: 
# 0, 30, 40, 50, 80, 150 và đếm số lượng phần tử ở mỗi nhóm.
cats1 = pd.cut(df['age'], bins=[0, 30, 40, 50, 80, 150])
label2 = ['poor', 'poor1', 'medium', 'rich1', 'rich2']
cats2 = pd.cut(df['MonthlyIncome'], bins=[0, 30, 40, 50, 80, 150.], labels=label2)
print(pd.value_counts(cats2))
print(cats2)