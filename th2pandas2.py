# Hợp nhất các dòng dữ liệu từ nhiều df
import pandas as pd
import numpy as np

df = pd.read_csv('FoodPrice_in_Turkey.csv')

df1 = df.loc[:4999, :]
df2 = df.loc[5000:, :]
# tách file3 chứa thông tin giá với số dòng từ bản ghi 1000-2000
df3 = df.loc[1000:2000, ['ProductId', 'Place', 'Month', 'Year', 'Price']]


## HỢP NHẤT CÁC DÒNG
# Cách 1: concat() cho phép ghép từ 2 df trở lên
# df mới bao gồm tất cả bản ghi của các df cần ghép
# pd.concat([df1, df2, ...], axis = 0)
df4 = pd.concat([df1, df2], axis=0)
# print(df4, end='\n\n')
df5 = pd.concat([df1, df2, df3], axis=0)
# print(df5)


# Cách 2: append() cho phép ghép 2 df lại
# df.append(other, ignore_index=False, verify_intergrity=Fasle, sort = None)
# other: danh sách các df
# ignore_index: mặc định False, True -> giá trị index sẽ không được sử dụng
df6 = df1.append(df2)
print(df6)