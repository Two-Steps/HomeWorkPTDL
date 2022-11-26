# câu hỏi bài tập lớn
# lọc dữ liệu nhiễu ntn ?
# chọn feature nào cho mô hình ?
# chọn mô hình nào ?
# có tối ưu nó nữa được hay không ?

# thêm key confusion_metrix ??? cách kiểm tra sai số như cái mean_absolute_error kia
# thêm mape ??

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error
# hãy xây dựng mô hình hồi quy tuyến tính theo các thông số rating_bad,
#  rating_good, rating_normal, rating_star
#b1: tạo dữ liệu
df = pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
# print(df.head())

#b2: chua dữ liệu ra train test val
target = df[['rating_good', 'rating_bad', 'rating_normal', 'rating_star']]
# print(target.head())
# xử lý dữ liệu nhiễu
target = target.dropna()
# shuffer dữ liệu - nhớ lại phần lấy dữ liệu mẫu trên data camp - sample
target = target.sample(frac= 1).reset_index(drop=True)
# print(target.head())
# chia 80/20 cho trainning va test
lenght = target.shape[0]
train_data = target.loc[0:int(lenght * 0.8)]
# print(train_data.head())
test_data = target.loc[int(lenght * 0.8):]

#b3: xây mô hình
model = LinearRegression()
x = train_data[['rating_bad','rating_good','rating_normal']]
y = train_data['rating_star']
model.fit(x, y)

#b4: đánh giá metrics
x_test = test_data[['rating_bad','rating_good','rating_normal']]
y_test = test_data['rating_star']
y_pred = model.predict(x_test)

err = mean_absolute_error(y_test, y_pred)
print(err)
#b5 infer với dữ liệu thực tế
# x_infer = np.array([[456, 23, 452]])
# print('infer: ', model.predict(x_infer))