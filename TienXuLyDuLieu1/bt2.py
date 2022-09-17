# Phân tích bộ dữ liệu HousePrice_DongDa
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler


df = pd.read_excel('house_price_dống-da.xlsx')

# Kiểm tra dữ liệu khuyết thiếu
# print(df.info())
# print(df.isna())
# Xóa bỏ hết tất cả những dòng dữ liệu không có thông tin về giá
df = df.dropna(subset=['price'])
# 3.Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu của 
# land_certificate bằng =”không có thông tin”,
# house_direction, balcony_direction, toilet, bedroom, Floor  
# bằng giá trị có tần số xuất hiện lớn nhất của các thuộc tính đó
df = df.fillna(value={'land_certificate':'Không có thông tin'})

list_ = ['house_direction', 'bedroom', 'balcony_direction', 'toilet', 'floor']

a = df['house_direction'].value_counts().index[0]
df = df.fillna(value={'house_direction':a})
a2 = df['bedroom'].value_counts().index[0]
df = df.fillna(value={'bedroom':a2})
a3 = df['balcony_direction'].value_counts().index[0]
df = df.fillna(value={'balcony_direction':a3})
a4 = df['toilet'].value_counts().index[0]
df = df.fillna(value={'toilet':a4})
a5 = df['floor'].value_counts().index[0]
df = df.fillna(value={'floor':a5})
# print(df.info())
# Lọc thông tin những bất động sản ở trong ngõ thành bộ dữ liệu nhà ngõ
df_nha_ngo = df
df_nha_ngo['type_of_land'] = df['type_of_land'].where(df['type_of_land'].str.contains('nhà riêng'))
df_nha_ngo.dropna(inplace=True)
df_nha_ngo['gia/m2'] = df_nha_ngo['price']/df_nha_ngo['area']
# print(df_nha_ngo)
Q1_area = df_nha_ngo['area'].quantile(0.25)
Q3_area = df_nha_ngo['area'].quantile(0.75)
IQR_area = Q3_area - Q1_area
# loại bỏ ngoại lai
df_nha_ngo['area'] = df_nha_ngo['area'].where(~(df_nha_ngo['area'] < (Q1_area - 1.5*IQR_area)) 
| (df_nha_ngo['area'] > (Q3_area + 1.5*IQR_area) ))

Q1_giam2 = df_nha_ngo['gia/m2'].quantile(0.25)
Q3_giam2 = df_nha_ngo['gia/m2'].quantile(0.75)
IQR_giam2 = Q3_giam2 - Q1_giam2
# loại bỏ ngoại lai
df_nha_ngo['gia/m2'] = df_nha_ngo['gia/m2'].where(~(df_nha_ngo['gia/m2'] < (Q1_giam2 - 1.5*IQR_giam2)) 
| (df_nha_ngo['gia/m2'] > (Q3_giam2 + 1.5*IQR_giam2) ))

# -------- 1. Chuẩn hóa gia/m2 với minmax scaling
scaler = MinMaxScaler()
mms = scaler.fit_transform(pd.DataFrame(df_nha_ngo['gia/m2']))
sns.kdeplot(data=mms)
plt.show()

# -------- 2. Chuẩn hóa gia/m2 với robust scaling
scaler_robust = RobustScaler()
rbs = scaler_robust.fit_transform(pd.DataFrame(df_nha_ngo['gia/m2']))
sns.kdeplot(data=rbs)
plt.show()

# -------- 3. Chuẩn hóa gia/m2 với standard scaling
scaler_standard = StandardScaler()
sc = scaler_standard.fit_transform(pd.DataFrame(df_nha_ngo['gia/m2']))
sns.kdeplot(data=sc)
plt.show()