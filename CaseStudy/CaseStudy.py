# "Xây dựng  mô hình dự báo giá nhà trên/m2 của bài toán mua bán nhà mặt phố Quận Hai Bà Trưng"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple
from sklearn.base import BaseEstimator, TransformerMixin

def find_boxplot_boundaries(
    col: pd.Series, whisker_coeff: float = 1.5
) -> Tuple[float, float]:
    Q1 = col.quantile(0.25)
    Q3 = col.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - whisker_coeff * IQR
    upper = Q3 + whisker_coeff * IQR
    return lower, upper


class BoxplotOutlierClipper(BaseEstimator, TransformerMixin):
    def __init__(self, whisker_coeff: float = 1.5):
        self.whisker = whisker_coeff
        self.lower = None
        self.upper = None

    def fit(self, X: pd.Series):
        self.lower, self.upper = find_boxplot_boundaries(X, self.whisker)
        return self

    def transform(self, X):
        return X.clip(self.lower, self.upper)

df = pd.read_csv('CaseStudy\RoadSurfaceHouseTrading.csv')
# print(df.head(5))
# print(df.info())
# print(df.describe())

# print(df['do_rong_duong_ml'].value_counts())
# lấy danh sách căn hộ có ten_quan là: Hai Bà Trưng / Quận Hai Bà Trưng và do_rong_duong_ml là: Mặt phố - Mặt đường
df = df[((df['ten_quan'] == 'Hai Bà Trưng') | (df['ten_quan'] == 'Quận Hai Bà Trưng')) & (df['do_rong_duong_ml'] == 'Mặt phố - Mặt đường')]
# print(df.head())
# print(df.info())
# print(df.describe())

# print(df.columns)
# ['Unnamed: 0', 'dien_tich', 'huong_ban_cong', 'phong_ngu',
#        'id_thanh_pho', 'ten_thanh_pho', 'id_quan', 'ten_quan', 'so_tang',
#        'mat_tien', 'noi_that', 'huong_nha', 'so_do', 'lat', 'long', 'gia',
#        'gia_m2', 'du_an', 'project_name', 'id_duong', 'ten_duong',
#        'do_rong_duong', 'do_rong_duong_ml', 'id_phuong', 'ten_phuong']

# tạm thời bỏ một số cột mà gần như chắc chắn k liên quan cho bớt rối mắt đã nào
list_columns = ['dien_tich', 'phong_ngu','so_tang', 'mat_tien', 'noi_that', 'huong_nha', 'so_do', 'lat', 'long', 
'gia','gia_m2', 'id_duong', 'ten_duong','do_rong_duong', 'id_phuong', 'ten_phuong']
df = df[list_columns].reset_index(drop= True)
# print(df.head())
# print(df.info())
# print(df.describe())
# df.to_csv('data_report.csv')
# plt.figure(figsize=(18,5))
# sns.heatmap(df.corr(), annot=True, lw = 1, linecolor="r",cmap="coolwarm")
# plt.show()

# tạm thời chưa xác định được hoàn toàn các feature, nên đành để tạm vậy @@ 

# xử lý cột đầu tiên: dien_tich  5644 non-null/ 5688 row
# print(df['dien_tich'].describe())
# min = 2 ?? max = 9393 ?? trong khi quantile(0.5) = 70 => có vấn đề với giá trị ngoại lai
# => xóa bỏ các giá trị nan trong diện tích
df1 = df.dropna(subset= ['dien_tich']) # drop na
# print(df1['dien_tich'].describe())
# df1['dien_tich'].hist(bins = 100)
# plt.show()
df1['dien_tich'] = BoxplotOutlierClipper().fit_transform(df1['dien_tich'])
# print(df1['dien_tich'].describe())
# df1['dien_tich'].hist(bins = 100)
# sns.boxplot(data= df1['dien_tich'])
# plt.show()
# df1.to_csv('data_report.csv')

# # xử lý cột thứ hai: huong_ban_cong ?? quá ít dữ liệu để có thể điền vào phần thiếu => drop cột này
# # xóa luôn từ dòng code 28

# print(df1.info())
# xử lý cột thứ 3: phong_ngu 3057 non-null/ 5288 row - update: mới sủa lại code chưa chắc số bản ghi đã chuẩn
print(df1['phong_ngu'].describe())
# sns.histplot(data= df1['phong_ngu'], bins= 100)
# plt.show()
df1['phong_ngu'] = BoxplotOutlierClipper().fit_transform(df1['phong_ngu'])
# sns.histplot(data= df1['phong_ngu'], bins= 10)
# sns.boxplot(data= df1['phong_ngu'])
# plt.show()
# print(df1['phong_ngu'].describe())
df1['phong_ngu'] = df1['phong_ngu'].fillna(df1['phong_ngu'].mean())
print(df1.info())
# print(df1['phong_ngu'].describe())
# df1.to_csv('data_report.csv')

# # xử lý cột số tầng 4087 non-null non-null / 5644 row - đã update số bản ghi ở đây
print(df1['so_tang'].describe())
# sns.histplot(data= df1['so_tang'], bins = 600)
# plt.show()
# sns.boxplot(data = df1['so_tang'])
# plt.show()

df1['so_tang'] = BoxplotOutlierClipper().fit_transform(df1['so_tang'])
# sns.boxplot(data = df1['so_tang'])
# plt.show()
df1['so_tang'] = df1['so_tang'].fillna(df1['so_tang'].mean()) # fill na
# df1['so_tang'].hist(bins= 10)
# plt.show()
print(df1['so_tang'].describe())
print(df1.info())
df1.to_csv('data_report.csv')
