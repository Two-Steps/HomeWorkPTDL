# Thực hành trên bộ dữ liệu Online Retail
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

df = pd.read_csv('OnlineRetail.csv')
print(df.shape)
print(df.info())
# Kiểm tra dữ liệu bị khuyết thiếu
# print(df.isna())
# Kiểm tra dữ liệu không bị khuyết thiếu
df['CustomerID'].notna()
# In những dòng ngoại lai Quantity < 0
df[df['Quantity'] < 0]
# Xóa bỏ những dòng ngoại lai của Quantity
df = df[df['Quantity'] >= 0]
# Xóa những dòng chứa giá trị khuyết thiếu
df1 = df.dropna()
# print(df1.shape)
# Xóa những dòng chứa toàn giá trị khuyết thiếu
df2 = df.dropna(how='all')
# print(df2.shape)
# Giữ những dòng có ít nhất 7 giá trị k bị khuyết thiếu
df3 = df.dropna(thresh=7)
# print(df3.shape)
# Xóa những dòng mà có giá trị khuyết thiếu trên cột CustomerID
df4 = df.dropna(subset=['CustomerID'])
# print(df4.shape)

# Thay thế giá trị bị khuyết thiếu trên cột CustomerID = -1
df5 = df
df5['CustomerID'] = df['CustomerID'].fillna(-1)
# Hiển thị những dòng vừa đc thay thế 
# print(df5[df5['CustomerID'] == -1])
# Thay thế các giá trị khuyết thiếu ở cột Country = giá trị trước đó
df5['Country'] = df['Country'].fillna(method='ffill')
# print(df5)

# -------------- Xử lý ngoại lai ---------------------
# sns.boxplot(x=df1['Quantity'])
# plt.show()
Q1 = df1['Quantity'].quantile(0.25)
Q3 = df1['Quantity'].quantile(0.75)
IQR = Q3 - Q1
# xác định phần tử không phải ngoại lai
df6 = df1
df6['outlier'] = ~((df1['Quantity'] < (Q1 - 1.5*IQR)) 
                | (df1['Quantity'] > (Q3 + 1.5*IQR)))
# xóa phần tử ngoại lai
df6 = df6[df6['outlier'] == True]
# sns.boxplot(x=df6['Quantity'])
# plt.show()

# ------------- Chuẩn hóa dữ liệu ---------------
# mô tả dữ liệu
# df1['Quantity'].describe()
# # chuẩn hóa dữ liệu với minmax scaling
# scaler = MinMaxScaler()

# # Chuẩn hóa dữ liệu trong df với MinMaxScaler ở 2 cột Quantity và UnitPrice
# df_s = scaler.fit_transform(df1[['Quantity']])
# # mô tả dữ liệu sau chuẩn hóa
# pd.DataFrame(df_s).describe()

# chuẩn hóa dữ liệu với robust scaling
# scaler = RobustScaler()

# # Chuẩn hóa dữ liệu trong df với RobustScaler ở 2 cột Quantity và UnitPrice
# df_s = scaler.fit_transform(df1[['Quantity']])
# # mô tả dữ liệu sau chuẩn hóa
# pd.DataFrame(df_s).describe()
# chuẩn hóa dữ liệu với z-score scaling
scaler = StandardScaler()

# Chuẩn hóa dữ liệu trong df với StandardScaler ở 2 cột Quantity và UnitPrice
df_s = scaler.fit_transform(df1[['Quantity']])
# print(pd.DataFrame(df_s).describe())
# sns.boxplot(x=df_s)
sns.kdeplot(data=df_s)
plt.show()

# ------------------- Mã hóa dữ liệu ----------------
# các giá trị ở cột Country
df1['Country'].unique()
# mã hóa cột Country với One-hot encoder sử dụng scikit learn
encoder = OneHotEncoder()

encoded_data = encoder.fit_transform(np.asarray(df1['Country']).reshape(-1,1))
encoded_data.todense()

# mã hóa cột Country với One-hot encoder sử dụng pandas
pd.get_dummies(df1['Country'])

# mã hóa cột Country với Label encoder sử dụng scikit learn
encoder = LabelEncoder()

encoded_data = encoder.fit_transform(np.asarray(df1['Country']))
encoded_data

# mã hóa cột Country với Label encoder sử dụng pandas
df1['Country'].astype('category').cat.codes

# -------------- Rời rạc hóa dữ liệu ---------------
# Rời rạc hóa dữ liệu ở cột UnitPrice

# chia thành 4 khoảng giá trị có độ dài bằng nhau
cats = pd.cut(df1['UnitPrice'], 4)
# số lượng phần từ ở mỗi phần
pd.value_counts(cats)

# chia thành 4 phần có số lượng phần tử tương đương nhau
cats2 = pd.qcut(df1['UnitPrice'], 4)
# số lượng phần từ ở mỗi phần
pd.value_counts(cats2)