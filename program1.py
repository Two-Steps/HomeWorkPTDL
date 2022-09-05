# [Thực hành] Thực hành trên bộ dữ liệu Online Retail

import pandas as pd

df = pd.read_csv('OnlineRetail.csv')
# xem 5 dong dau 
# print(df.head())

# xem thong tin bo du lieu
# print(df.info())

# cong ty ban hang tai bao nhieu quoc gia
country = df.Country.unique()
print('So luong quoc gia: ' + str(country.size))

# so luong don hang ban ra va tong doanh thu

## tạo cột tính thành tiền của các mặt hàng
df['total'] = df['Quantity'] * df['UnitPrice']
# print(df.head())

## giá trị đơn hàng của mỗi đơn hàng
total_invoices = df['total'].sum()
print('số lượng hóa đơn bán ra: ' + str(total_invoices.size))
print('tổng doanh thu: ' + str(total_invoices))

# top 10 mặt hàng có số lượng bán ra lớn nhất
quantity_product = df.groupby(['StockCode', 'Description'])['Quantity'].sum().sort_values(ascending= False)
print(quantity_product.head(5))

# top 10 mặt hàng có doanh thu lớn nhất

total_money = df.groupby(['StockCode', 'Description'])['total'].sum().sort_values(ascending= False)
print(total_money.head(10))
