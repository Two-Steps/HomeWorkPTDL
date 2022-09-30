# Vẽ đồ thị kết hợp – Online Retail
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('OnlineRetail.csv')
# print(df.head())

# 1.Biểu đồ đường thể hiện doanh thu theo từng tháng năm 2011.
# 2.Biểu đồ cột thể hiện số lượng đơn hàng trong các tháng của năm 2011.

#chuyển InvoiceDate thành datetime object
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
#lấy các cột dữ liệu cần thiết
d1 = df[['InvoiceNo', 'InvoiceDate', 'Quantity', 'UnitPrice']] 
#tính doanh thu trên mỗi row
d1['Revenue'] = d1['Quantity'] * d1['UnitPrice'] 
#chuyển mỗi giá trị InvoiceDate thành index của mỗi để search theo index
d1 = d1.set_index(['InvoiceDate']) 
#lọc những hàng mà index có chứa '2011'
d2 = d1['2011'] 
d2 = d2.reset_index()
#tính tổng doanh thu theo tháng
d3 = d2.groupby(by=d2['InvoiceDate'].dt.month).sum() 
# xóa bỏ các dòng trùng lặp của cùng một đơn hàng
d4 = d1.drop_duplicates(subset = 'InvoiceNo', keep = 'first') 
d4 = d4['2011']
d4 = d4.reset_index()
#đếm tổng số đơn hàng trong tháng
d5 = d4.groupby(by=d4['InvoiceDate'].dt.month).count() 

x = d5.index.get_level_values(0)
plt.bar(x, d5['InvoiceNo'], width = 0.5, label = 'InvoiceNo')
axes1 = plt.gca()
axes2 = axes1.twinx()
axes2.plot(x, d3['Revenue'], label = 'Revenue', linewidth = 2, c = 'r', marker = 'o')
axes1.set_xlabel('Month', fontsize = 14)
axes1.set_ylabel('#Invoices', fontsize = 14)
axes2.set_ylabel('$', fontsize = 14)

axes1.legend(fontsize = 14)
axes2.legend(fontsize = 14)
plt.title('#Invoices and Revenue in 2011', fontsize = 16)
plt.show()