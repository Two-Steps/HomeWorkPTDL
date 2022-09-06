# thực hành trên bộ dữ liệu GDP List
import pandas as pd
import numpy as np

df = pd.read_csv('GDPlist.csv', encoding='latin1')
# print(df.head())
# print(df.columns)
# ['Country', 'Continent', 'GDP (millions of US$)']

# print('Số dòng: ' + str(df.shape[0]))
# print('Số cột: ' + str(df.shape[1]))
# print(df.info())

df.rename(columns={'Country':'Nuoc', 'Continent':'Chauluc', 'GDP (millions of US$)':'GDP (trieu $)'}, inplace=True)
print(df.head())
print()

# - Thêm cột mới 'Thanhpho' sau cột 'Nuoc', giá trị là giá trị của cột nước
# df.insert(1,'Thanhpho',df['Nuoc'])
df.insert(1, 'Thanhpho',df.loc[:,'Nuoc'])
print(df.head())

# - Trong cột 'Thanhpho' thay giá trị VietNam thành Hanoi
# df['Thanhpho'].replace('Vietnam','Hanoi', inplace=True)
# - cách trên k được, phải chăng có 1 khoảng trống hay ký tự nào đó trong
# giá trị Vietnam cần thay thế ? OK tìm hiểu regex xem đc k nhé
df['Thanhpho'].replace(to_replace= r'Vietnam$', value='Hanoi', regex=True, inplace=True)
vn = df.loc[122]
print(vn)

# - Xóa các bản ghi có châu lục là 'Asia'
df.drop(df.loc[df['Chauluc'] == 'Asia'].index, axis=0, inplace=True)
print(df.head())

# - Xóa các bản ghi có GDP < 300000
print()
df.drop(df.loc[df['GDP (trieu $)'] < 300000].index, axis=0, inplace=True)
print(df.head())

