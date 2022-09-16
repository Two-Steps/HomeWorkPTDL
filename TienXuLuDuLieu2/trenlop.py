import pandas as pd 
import numpy as np
from sklearn.preprocessing import OneHotEncoder

list_ = ['red', 'red', 'yellow', 'green', 'yellow']
# print(list_)

# Biến list thành dataframe
data = pd.DataFrame(list_, columns=['color'])
# print(data)

# Encoding cột color
encoder = OneHotEncoder(sparse=False) # Tạo object encoder
onehot = encoder.fit_transform(data)
# print(onehot) # trả về một mảng 2 chiều

# Cách 2 sử dụng hàm có sẵn
# print(pd.get_dummies(data))

### Label encoding

# Cách 1: Dùng sklearn
# Dùng cho dữ liệu 1 chiều
from sklearn.preprocessing import LabelEncoder
encoder1 = LabelEncoder() # Đặt object
lb = encoder1.fit_transform(data.loc[:, 'color'])
# print(lb)

# Cách 2: 
# Dùng hàm của pandas -> chỉ dùng cho Series
# Phải ép kiểu về 'category'
data.loc[:, 'color'] = data.loc[:, 'color'].astype('category').cat.codes
# print(data)

# Exam
list2 = ['red', 'green', 'pink', 'yellow', 'orange', 'green', 'red', 'yellow']
# hãy encode list trên theo 3 cách
df2 = pd.DataFrame(list2, columns=['color'])
#1.Sử dụng sklearn
# encode3 = LabelEncoder()
# lb3 = encode3.fit_transform(df2.loc[:, 'color'])
# print(lb3)

#2.Sử dụng hàm có sẵn của pandas
# df2.loc[:, 'color'] = df2.loc[:, 'color'].astype('category').cat.codes
# print()
# print(df2)

#3. Làm thủ công xuất ra 1 cột mới bên cạnh cột color, giá trị xuất phát từ 1

# conditions = [(df2['color'] == 'red'), 
#               (df2['color'] == 'green'),
#               (df2['color'] == 'pink'),
#               (df2['color'] == 'yellow'),
#               (df2['color'] == 'orange')]
# choices = [1, 2, 3, 4, 5]
# df2['encode'] = np.select(conditions, choices, default= 'NaN')
# print(df2)

# Cách khác sử dụng cái này nha :)) lười học nó quen
# df2['aaa'] = [1, 4, 5, 6, 7, 7, 5, 8]

print()
# Cách của thầy
# chuyển nó sang dataframe đã nhé, ở đây ăn sẵn df2
# u = df2.iloc[:, 0].unique()
# print(u)
# print()
# df2.loc[:, 'encoded'] = np.nan
# for ind, val in enumerate(u):
#     df2.loc[df2.loc[:, 'color'] == val, 'encoded'] = ind + 1
# print(df2)


#### Ordinal encoding
from sklearn.preprocessing import OrdinalEncoder
# list3 = ['excellent', 'very_good', 'good', 'normal', 'bad']
# print(list3)
# df3 = pd.DataFrame(list3, columns=['rate'])
# print(df3)
# encode4 = OrdinalEncoder()
# oe1 = encode4.fit_transform(df3)
# print(oe1) 
# print mặc định theo abc

encode5 = OrdinalEncoder()
# list reverse()
# encode5.categories = [np.array(list3)]
# oe3 = encode5.fit_transform(df3)
# print(oe3)

df_price = pd.read_csv('FoodPrice_in_Turkey.csv', header=0)
print(df_price)
# mã hóa productname với one-hot
encoder_productName = OneHotEncoder(sparse=False) # Tạo object encoder
onehot = encoder_productName.fit_transform(df_price.loc[:, ['ProductName']])
print(encoder_productName) # trả về một mảng 2 chiều
