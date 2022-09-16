import pandas as pd
import numpy as np

df = pd.read_excel('house_price_dống-da.xlsx')
# print(df.columns)
# ['title', 'address', 'area', 'price', 'postDate', 'land_certificate',
# 'house_direction', 'balcony_direction', 'toilet', 'bedroom', 'floor',
# 'type_of_land', 'street_name', 'ward_name', 'district_name',
# 'city_name', 'lat', 'long']
# print('Số dòng: ' + str(df.shape[0]) )
# print('Số cột: ' + str(df.shape[1]) )
# print(df.info())

# 2.Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên
df1 = df[df['address'].str.contains('Trung Liệt|Khâm Thiêm')]
# print(df1)

# 3.Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của 
# các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên
df2 = df.query('(land_certificate == "Sổ đỏ") and (bedroom >= 3)')\
        .filter(['address', 'price', 'house_direction', 'balcony_direction'])
# print(df2)

# 4.Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất
df['type_of_land'] = df['type_of_land'].str.strip()
avg_price = df.groupby('type_of_land')['price'].mean()
max_price = df.groupby('type_of_land')['price'].max()
min_price = df.groupby('type_of_land')['price'].min()
# print('avg of price', avg_price, sep='\n\n', end='\n\n')
# print('max of price', max_price, sep='\n\n', end='\n\n')
# print('min of price', min_price, sep='\n\n', end='\n\n')

# 5.Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.
df['ward_name'] = df['ward_name'].str.strip()
avg_bedroom = df.groupby(['ward_name'])['bedroom'].mean()
avg_toilet = df.groupby(['ward_name'])['toilet'].mean()
avg_floor = df.groupby(['ward_name'])['floor'].mean()
