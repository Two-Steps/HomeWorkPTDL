# Hợp nhất các cột dữ liệu từ nhiều dataframe
import pandas as pd
import numpy as np

df = pd.read_csv('FoodPrice_in_Turkey.csv')
# print(df.head())
# print(df.columns)
# ['Place', 'ProductId', 'ProductName', 'UmId', 'UmName', 'Month', 'Year',      
#        'Price']

# - Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi
# cuối cùng, giữ chỉ số ban đầu của các dòng
# df = df.drop_duplicates(['ProductId'], keep='last')

# - Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi
# cuối cùng, thiết lập lại chỉ só
df = df.drop_duplicates(['ProductId'], keep='last').reset_index(drop=True)

# - Tách file chứ thông tin sản phẩm
df_pro = df.loc[:, ['ProductId', 'ProductName', 'UmId', 'UmName']]
# print(df_pro)

# - Tách file chứa thông tin giá
df_pri = df.loc[:, ['ProductId', 'Place', 'Month', 'Year', 'Price']]
# print(df_pri)

# - Tách file chứ thông tin giá với số dòng từ bản ghi 10-20
df_pri10 = df.loc[10:20, ['ProductId', 'Place', 'Month', 'Year', 'Price']]
# print(df_pri10)

### GHÉP CÁC CỘT TỪ FILE
# - Cách 1: merge() ghép 2 df có cùng chung một thuộc tính.
# df mới được tạo ta gồm các thuộc tính riêng và chung
# pd.merge(df1, df2, on = 'Tên thuộc tính chung')
df1 = pd.merge(df_pro, df_pri, on='ProductId')
print(df1)

# - Cách 2: concat() cho phép ghép từ 2 df trở lên với nhau
# các df không cần cột thuộc tính chung
# df mới chứa tất cả cột thuojc tính của các df ghép
#  pd.concat([df1, df2, ...], axis=1)
df2 = pd.concat([df_pro, df_pri], axis=1)
print(df2)