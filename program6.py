# chỉnh sửa cấu trúc bộ dữ liệu
import pandas as pd
import numpy as np

df = pd.read_csv('FoodPrice_in_Turkey.csv')
# print(df.head())

# /đổi tên cột

# print('-' * 80)
# df.rename(columns={'Place': 'Địa điểm', 'ProductName': 'Tên SP'}, inplace=True)
# # df.rename(index={0:'haha'}, inplace=True)
print(df.head())

# /thêm cột mới

print('-' * 80)
df['new column'] = np.nan
# # print(df.head())

# /thêm cột giảm giá 10% cho tất cả các bản ghi

print('-' * 80)
# cách 1: gán tên cột dưới dạng một chuỗi và thêm giá trị vào cột đó

df['Giảm giá'] = pd.Series('10%', index= df.index)
print(df.head())

# Cách 2: Sử dụng phương thức insert() gồm 3 đối số
# - đối số đầu tiên là chỉ mục (vị trí) muốn chèn cột mới 
# (chỉ mục là 10--> cột mới được thêm vào vị trí 11 của DataFrame)
# - đối số thứ hai là tên của cột mới muốn chèn 
# - đối số thứ ba giá trị của cột

df.insert(10, 'Giảm giá 2', pd.Series('12%', df.index))
print(df.head())

# /thêm dòng mới vào dataframe
# https://datagy.io/pandas-add-row/

# - Sử dụng phương thức append()
# -- nótè: ở đây đang test việc thêm thiếu cột nào đó và thêm thừa 1 cột k có trong df ban đầu
df = df.append({'Place':'NA', 'ProductId':'RR', 'ProductName':'Rice',
    'UmId':10, 'UmName':'KG', 'Month':6, 'Year':2021, 'Price':84.3785,
    'Giảm giá': '10%', 'haha':'test'}, ignore_index=True)

# -- nótè2: hoàn toàn có thể thêm 1 dòng mới bằng cách này
# đơn giản là truy cập hàng thứ n (sau hàng cuối - index ở đây chạy từ 0) rồi gán nó bằng 1 list
# lưu ý list này bắt buộc phải có số phần tử trùng với số cột chứ không bát nháo như append() được
df.loc[len(df)] = ['test1', 'test2', 3, 'haha', 'a', 'g', 'h', 'k', 'hgh','sfds','sdsfd', '12']
print(df.tail())

# /xóa một cột trong dataframe

# del df['new column]

# - Sử dụng phương thức pop()
# pop() trả về cột đã xóa

df.pop('Giảm giá 2')
print(df.head())

# - Sử dụng phương thức drop()
# Cú pháp: df.drop('column_name', axis=1, inplace=True)
# Trong đó axis = 1 là xóa cột; inplace = True xóa trục tiếp 
# trên dữ liệu gốc mà không phải tạo bản sao

df.drop(['Giảm giá', 'haha', 'new column'], axis=1, inplace=True)
print(df.head())

# /Xóa các dòng trong dataframe

# Cú pháp: df.drop(Chỉ số dòng cần xóa, axis=0, inplace=True)
# axis = 0 là giá trị mặc định có thể viết tường minh hoặc không
# Xóa dòng có chỉ số 1 (dòng thứ 2) sử dụng phương thức drop()

df.drop(1, axis=0, inplace=True)
print(df.head())