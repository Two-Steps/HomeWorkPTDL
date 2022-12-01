# "Xây dựng  mô hình dự báo giá nhà trên/m2 của bài toán mua bán nhà mặt phố Quận Hai Bà Trưng"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error, r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

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

df = pd.read_csv('CaseStudy\RoadSurfaceHouseTrading.csv', encoding='utf-8')
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

# tạm thời bỏ một số cột mà gần như chắc chắn k liên quan cho bớt rối mắt đã nào - update noi_that, huong nha bỏ, do_rong_duong => quá ít dữ liệu
list_columns = ['dien_tich', 'phong_ngu','so_tang', 'so_do', 'lat', 'long', 
'gia','gia_m2', 'id_duong', 'ten_duong', 'id_phuong', 'ten_phuong']
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
# print(df1['phong_ngu'].describe())
# sns.histplot(data= df1['phong_ngu'], bins= 100)
# plt.show()
df1['phong_ngu'] = BoxplotOutlierClipper().fit_transform(df1['phong_ngu'])
# sns.histplot(data= df1['phong_ngu'], bins= 10)
# sns.boxplot(data= df1['phong_ngu'])
# plt.show()
# print(df1['phong_ngu'].describe())
df1['phong_ngu'] = df1['phong_ngu'].fillna(df1['phong_ngu'].mean())
# print(df1.info())
# print(df1['phong_ngu'].describe())
# df1.to_csv('data_report.csv')

# # xử lý cột số tầng 4087 non-null non-null / 5644 row - đã update số bản ghi ở đây
# print(df1['so_tang'].describe())
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
# print(df1['so_tang'].describe())
# print(df1.info())
# df1.to_csv('data_report.csv')

# xử lý trước cái id_duong, ten_duong, id_phuong, ten_phuong
df1 = df1.dropna(subset=['id_duong', 'ten_duong', 'id_phuong', 'ten_phuong'])
# print(df1.info())
# df1['id_duong'] = df1['id_duong'].astype('category').cat.codes
df1['ten_duong'] = df1['ten_duong'].astype('category').cat.codes
# df1['id_phuong'] = df1['id_phuong'].astype('category').cat.codes
df1['ten_phuong'] = df1['ten_phuong'].astype('category').cat.codes
# check thấy mỗi id_duong tương đương ten_duong => bỏ bớt đi
del df1['id_duong']
del df1['id_phuong']


# ===> bỏ mat_tien, tuy dữ liệu khoảng 20% nhưng khi thử fill thì nó quá ảo @@ 
# tiếp theo đến  mat_tien 1469 non-null/ 5644 record còn lại
# sns.boxplot(data = df1['mat_tien'])
# plt.show()
# print(df1['mat_tien'].describe())
# df1['mat_tien'] = BoxplotOutlierClipper().fit_transform(df1['mat_tien'])
# # sns.boxplot(data = df1['mat_tien'])
# # plt.show()
# # print(df1['mat_tien'].describe())
# # df1.to_csv('data_report.csv')
# df1['mat_tien'] = df1['mat_tien'].fillna(0)
# a = df1.groupby(['ten_duong', 'id_duong'])['mat_tien'].mean()
# dic_mt = {} 
# for i in range(a.shape[0]):
#     if a.values[i] != 0:
#         dic_mt[a.index[i][0]] = a.values[i]
#     else:
#         dic_mt[a.index[i][0]] = a.values.mean()
# # print(dic_mt)
# for k, v in dic_mt.items():
#     index = df1.index[df1['ten_duong'] == k].tolist()
#     df1.loc[index, 'mat_tien'] = float(v)

# df1.to_csv('data_report1.csv')
# print(df1.info())

# xử lý phần sổ đỏ
def pre_sd(item):
    list_1 = ['sổ đỏ','số đỏ', 'sổ hồng','sổ nét', 'có sổ', 'sđcc','sdcc', 'riêng', 'đẹp', 'chuẩn', 'so do', 'chính chủ','sổ 1 chủ',\
         'sổ xịn', 'giấy phép', 'giấy tờ', 'pháp lý đầy đủ','pháp lí đầy đủ','đầy đủ pháp lý', 'sổ sách đàng hoàng', 'sẵn sàng giao dịch'\
            'sổ rất nét', 'sổ phân lô', 'só sổ']
    for i in list_1:
        if str(item).find(i) != -1:
            return 1
        elif str(item).find(i) == -1: 
            return 0

df1['so_do'] = df1['so_do'].str.lower()
df1['so_do'] = df1['so_do'].str.strip('- !. + , : , ) (')
df1['so_do2'] = df1['so_do'].apply(pre_sd)
# print(df1['so_do2'].value_counts())
del df1['so_do']
# df1.to_csv('report_data2.csv')
# print(df1.info())

# xử lý cột giá
df1 = df1.dropna(subset= 'gia')
# print(df1.info())
# print(df1['gia'].describe())
# sns.boxplot(data= df1['gia'])
# plt.show()
df1['gia'] = BoxplotOutlierClipper().fit_transform(df1['gia'])
# print(df1['gia'].describe())
# print(df1.info())
# sns.boxplot(data= df1['gia'])
# plt.show()

# lat, long, gia/m2 ?
df1 = df1.dropna(subset = ['lat', 'long', 'gia_m2'])
# print(df1.info())
# print(df1.head(10))

# split dữ liệu
X, y = df1[['dien_tich', 'phong_ngu', 'so_tang', 'lat', 'long', 'gia', 'ten_duong', 'ten_phuong', 'so_do2']], df1['gia_m2']
X_train, X_test , y_train, y_test = train_test_split(X, y, train_size=0.8, test_size= 0.2, random_state= 0)
# print(X_train.head(10))
# print(y_train.head(10))
# regressor = LinearRegression()  # Khai báo mô hình hồi quy tuyến tính
# regressor.fit(X_train, y_train) #Huấn luyện mô hình

# y_pred = regressor.predict(X_test)
# r2 = r2_score(y_test, y_pred)
# print('r2: ', r2)
# print("MAPE: ",mean_absolute_percentage_error(y_test, y_pred))

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("MAPE: ",mean_absolute_percentage_error(y_test, y_pred))
