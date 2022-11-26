# Chọn đặc trưng nào để đưa vào mô hình ??? 
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd 
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

# Công ty ô tô Geely Auto của Trung Quốc muốn gia nhập thị trường Mỹ bằng cách thành lập
# nhà máy sản xuất của họ ở Mỹ để tạo sức cạnh tranh với các đối thủ Mỹ và Châu âu tại thị
# trường Mỹ. Công ty Geely Auto đã ký hợp đồng với một công ty tư vấn ôtô để tìm hiểu các
# yếu tác động tới giá ô tô. Cụ thể họ muốn tìm hiểu các đặc điểm của một chiếc xe sẽ ảnh
# hưởng tới việc định giá ô tô tại thị trường Mỹ, vì có thể thị hiếu của người tiêu dùng Mỹ có
# điểm khác biệt so với người tiêu dùng ở Trung quốc. Công ty muốn biết:

# Có những thuộc tính nào có ý nghĩa trong việc định giá của một chiếc xe hơi
# Các thuộc tính đó có liên hệ với giá xe như thế nào
# Dựa trên các cuộc khảo sát thị trường, công ty tư vấn đã thu thập một tập dữ liệu về các loại
# ô tô khác nhau trên thị trường Mỹ để phân tích.
# Bộ dữ liệu gồm các thuộc tính sau:

# car_ID : Mã xe
# symboling: Mức độ an toàn (giá trị trong khoảng từ 2 tới 3, trong đó giá trị -2: tuyệt đối an toàn, 3: có rủi ro)
# carName: Tên xe
# fueltype: Loại nhiên liệu
# aspiration: loại hút (turbo hoặc std)
# doornumber: Số lượng cửa
# carbody: Loại thân xe (sedan, wagon, hatchback)
# drivewheel: Loại bánh xe
# enginelocation: Vị trí động cơ
# wheelbase: Chiều dài cơ sở
# carlength: Chiều dài xe
# carwidth: Chiều rộng xe
# carheight: Chiều cao xe
# curbweight: Trọng lượng của xe khi không có người hoặc hành lý
# enginetype: Loại động cơ
# cylindernumber: Số lượng xi lanh đặt trong xe
# enginesize: Kích thước động cơ
# fuelsystem: Hệ thống nhiên liệu của xe ô tô
# boreratio: Tỉ số hành trình
# stroke: số kỳ hoăc kích thước bên trong động cơ
# compressionratio: Tỉ số nén của ôtô
# horsepower: Mã lực
# peakrpm: Tốc độ động cơ cao nhất
# citympg: số dặm đi được cho 1 galon (~4.5 l) nhiên liệu trong thành phố
# highwaympg: số dặm đi được cho 1 galon (~4.5 l) nhiên liệu trên đường cao tốc
# price: Giá xe

df = pd.read_csv('Case_study_CarPrice_Assignment.csv')
# print(df.info())
# print(df.describe())

# Tìm mối liên hệ giữa hãng xe và tên xe, phát hiện và sửa sai dữ liệu ???

#                                       BƯỚC 1: chọn feature

# print(df.corr(method='spearman')) # hiện tất cả mối tương quan giữa các dữ liệu, thêm cái para method kia
# không show ra được mối tương quan giữa mấy thuộc tính định lượng với category đâu nhé @@ 
# => encode má ơi

# prepprocessing
# tên xe(str), số cửa, chiều dài, mã lực, nguyên liệu(str), độ an toàn
df['BrandName'] = df.apply(lambda x : str(x['CarName']).split(' ')[0], axis= 1).reset_index(drop= True)
# print(df['BrandName'])

# def brand_name_process(df, column):
#     unique_brand = pd.unique(df[column]).tolist()
#     print(unique_brand)
#     print(len(unique_brand))
#     print(df['BrandName'].head(5))
#     for idx, brand_name in enumerate(unique_brand):
#         # df[df[column] == brand_name] = idx
#         for i in range(df.shape[0]):
#             if df.loc[i, column] == brand_name:
#                 df.loc[i, column] = idx
#     return df

def brand_name_process(df, column):
    unique_brand = pd.unique(df[column]).tolist()
    for idx, brand_name in enumerate(unique_brand):
        index = df.index[df[column] == brand_name].tolist()
        print(index)
        df.loc[index, column] = int(idx)
    return df 
# brand_name_process(df, 'BrandName')

# xử lý theo thư viện pandas =>> cần thiết dữ liệu phải cố định, không thay đổi
df['BrandName'] = df['BrandName'].astype('category').cat.codes

print(df.head(5))
# print(pd.unique(df['CarName']).tolist())

# dùng các trường sau để dự đoán sau khi df.corr()
# carwidth, curbweight, enginesize, citympg, hightwaympg, BrandName

#                   BƯỚC 2: loại bỏ nhiễu
# => cực kỳ quan trọng: boxplot , loại bỏ bớt dữ liệu ?
# cột đấy đủ dữ liệu k ? có nên xóa hay có thể điền
# => ở đây dữ liệu ăn sẵn nên đã sạch không cần làm gì

df[['carwidth','curbweight','enginesize','citympg','highwaympg','BranchName', 'price']]
# print(target.head(5))
target = df[['carwidth','curbweight','enginesize','citympg','highwaympg','BranchName', 'price']]


#                   BƯỚC 3: normalize data 

#                   BƯỚC 4: chọn mô hình
# linear, randomforest, bootrap ??
# metrics sklearn regression => gg cái này

# split du lieu
X, y = target[['carwidth','curbweight','enginesize','citympg','highwaympg','BranchName']], df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)

pred = regressor.predict(X_test)
print("MAPE: ",mean_absolute_percentage_error(y_test, pred))
# metrics

# b5: finuntune hyperparameter?? girdsearch, fintune cac thong so mo hinh 

from sklearn.model_selection import GridSearchCV

param_grid = [
    {'n_estimators': [3, 10], 'max_features': [2, 4, 6]},
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
]
grid_search = GridSearchCV(regressor, param_grid, cv=2,
                           scoring='neg_mean_squared_error',
                           refit=True)

grid_search.fit(X_train, y_train)

grid_search.best_params_.predict(X_test)
print("MAPE: ",mean_absolute_percentage_error(y_test, pred))


#                   BƯỚC 5: fintune hyperparameter các thông số mô hình gridsearch ??
