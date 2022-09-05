# truy cập dữ liệu trong dataframe

import pandas as pd
import numpy as np

df = pd.read_csv('FoodPrice_in_Turkey.csv')

print(df.head())

# / Sử dụng iloc để truy cập

# truy cập dòng có chỉ số 3
# print()
# tg = df.iloc[3]
# print(tg)
# # truy cập các dòng có chỉ số từ 3 đến 8
# print()
# tg2 = df.iloc[3:8]
# print(tg2)
# # truy cập các dòng rời rạc
# print()
# tg3 = df.iloc[[3, 5, 1]]
# print(tg3)

# # -Truy cập cột thứ 4 của dữ liệu
# # : được sử dụng để đại diện cho tất cả các dòng.
# print()
# c1 = df.iloc[:, 4]
# print(c1)

# print()
# c2 = df.iloc[:, 3:8]
# print(c2)

# - Truy cập phần tử tại dòng 3, cột 7
# print()
# x = df.iloc[3, 7]
# print(x)

# # - Truy cập các phần tử dòng 3 đến dòng 4, cột 5 đến cột 6
# x2 = df.iloc[3:5, 5:7]
# print(x2)

## Sử dụng phương thức loc để truy cập dữ liệu loc có thể làm việc được với 
# chỉ số hàng,tên cột và các biểu thức điều kiện của cột

# - Truy cập dòng có chỉ số 3 của dữ liệu
# print()
# a = df.loc[3]
# print(a)
# # - Truy cập cột thứ 4 của dữ liệu
# a2 = df.loc[:, 'UmName']
# print(a2)

# # - Truy cập cột thứ 4, 5
# a3 = df.loc[:, ['UmName', 'Month']]
# print(a3)

# # - Truy cập phần tử thứ 3 cột thứ 7
# a4 = df.loc[3, 'Price']
# print(a4)

# # - Truy cập phần tử có Year >= 2019
# a5 = df.loc[df['Year'] >= 2019]
# print(a5)

## Thay thế các giá trị trong dataframe

# - Thay số 5 bằng số 10 trong toàn bộ dữ liệu
df.replace(5, 10, inplace=True)
print(df.head())

# - Thay giá trị 10 trong cột Month thành giá trị 5
print()
df['Month'].replace(10, 5, inplace=True)
print(df.head())