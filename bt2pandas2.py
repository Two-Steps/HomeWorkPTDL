# Phân tích trên bộ dư liệu Online Retail
# Luyện tập Pivot Table
import pandas as pd
import numpy as np

df = pd.read_csv('OnlineRetail.csv')
df['InvoiceDate'] = df['InvoiceDate'].str.slice(0, -5)
print(df)
# print(df.columns)
# ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
# 'UnitPrice', 'CustomerID', 'Country']
# print(df.head())

# print('Số dòng: ', df.shape[0])
# print('Số cột: ', df.shape[1])
# print(df.info())

df1 = df.pivot_table(values='Quantity', index='InvoiceNo', columns='Country', aggfunc='mean')
# print(df1)

# -Xây dựng bảng Pivot table, với mỗi Khách hàng cho biết số lượng 
# mua hàng lớn nhất và nhỏ nhất theo Kho.
df2 = df.pivot_table(values='Quantity', index='StockCode', columns='CustomerID', aggfunc={min, max})
# print(df2)

# -Xây dựng bảng Pivot table, với mỗi Mã kho tính tổng số lượng 
# các mặt hàng và trung bình cộng giá.
df3 = df.pivot_table(values=['UnitPrice', 'Quantity'], index='StockCode',
        aggfunc={'UnitPrice': np.mean, 'Quantity': np.sum})
# print(df3)

# -Xây dựng bảng Pivot table cho biết tổng số lượng hàng bán được của mỗi ngày
df4 = df.pivot_table(values='Quantity', index= 'InvoiceDate',
        aggfunc={sum})
print(df4)