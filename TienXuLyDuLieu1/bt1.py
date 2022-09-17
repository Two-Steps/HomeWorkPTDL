# Phân tích bộ dữ liệu Online Retail
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler


df = pd.read_csv('OnlineRetail.csv')
# print(df.head())
# print(df.columns)
# ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
# 'UnitPrice', 'CustomerID', 'Country']
# print(df.info())

# print(df.isna())

# 2.Có nên xóa hết các dòng chứa dữ liệu khuyết thiếu, giải thích vì sao
# -> không nên xóa, dữ liệu khuyết thiếu ở cột Description và CustomerID
# mô tả sản phẩm thì có thể k cần có cũng đc, còn CustomerID là mã khách hàng
# có thể là những khách hàng mua lẻ hay họ không cung cấp thông tin

# 3. Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu của 
# thuộc tính Description bằng giá trị mặc định “Không biết”
df.fillna(value={'Description':'Không biết'}, inplace=True)
# print(df.info())

# 4.Thực hiện phát hiện giá trị ngoại lai của thuộc tính Quantity 
# và Thuộc tính UnitPrice
# -------------
# Với Quantity ta sẽ dùng Z-Score và BoxPlot để phát hiện điểm ngoại lai
# sns.boxplot(df['Quantity'])
# plt.show()
# -> nhìn vào biểu đồ Boxplot ta nhận định sơ qua là những điểm
# < -6500 và > 6000 là khả năng là ngoại lai
from scipy import stats
z_score = np.abs(stats.zscore(df['Quantity']))
# print(z_score)
# <==> Xử lý ngoại lai
# giả sử điểm có z-socre > 3 sẽ là ngoại lai
threshold = 3
# print(np.where(z_score > threshold)) # mảng các chỉ số dòng có ngoại lai,
# nếu khi tính z-socre ta truyền vào df thay vì cột thì ra 2 mảng chứ chỉ 
# số hàng và cột
# print(z_score[4287]) -> in thử ra coi có đúng k và nó đúng là > 3
inds = np.where(z_score < threshold)
df['Quantity'] = df.loc[inds, 'Quantity']
df.dropna(subset=['Quantity'], inplace=True)
# print(df['Quantity'])

# -------------
# Với UnitPrice ta sẽ dùng IQR score
Q1 = df['UnitPrice'].quantile(0.25)
Q3 = df['UnitPrice'].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
print(df['UnitPrice'])
print(df['UnitPrice'].min())
print(df['UnitPrice'].max())
df['UnitPrice'] = df['UnitPrice'].where(~(df['UnitPrice'] < (Q1 - 1.5*IQR)) | (df['UnitPrice'] > (Q3 + 1.5*IQR) ))
print(df['UnitPrice'])
print(df['UnitPrice'].min())
print(df['UnitPrice'].max())
