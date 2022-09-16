# Phân tích review của khách hành Credit_scoring
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

df = pd.read_csv('TienXuLyDuLieu1\Credit_Scoring.csv')
# print(df.columns)
# SeriousDlqin2yrs: Khách hàng gặp khó khăn tài chính trong vòng 2 năm
# trở lại đây
# Age: Tuổi
# Total_money: Tổng số dư trong tài khoản – tổng các khoản vay 
# NumberOfTime30-59DaysPastDueNotWorse: Số lần nợ thành toán thẻ từ 30-59 ngày.
# DebtRatio: Số tiền chi tiêu thẻ tín dụng/tổng thu nhập.
# MonthlyIncome: Thu nhập hàng tháng.
# NumberOfOpenCreditLinesAndLoans: Số lượng khoản vay Mở (trả góp như 
# khoản vay mua ô tô hoặc thế chấp) và Dòng tín dụng (ví dụ: thẻ tín dụng).
# NumberOfTimes90DaysLate: Số lần người vay đã quá hạn 90 ngày trở lên.
# NumberRealEstateLoansOrLines: Số lượng các khoản vay thế chấp và bất động
#  sản bao gồm hạn mức tín dụng sở hữu nhà.
# NumberOfTime60-89DaysPastDueNotWorse: Số lần người vay đã quá hạn 
# 60-89 ngày nhưng không tệ hơn trong 2 năm qua.
# NumberOfDependents: Số người phụ thuộc trong gia đình không bao gồm 
# bản thân

# print(df.info())
# ---- Xử lý dữ liệu khuyết thiếu -----

# 1.Kiểm tra dữ liệu khuyết thiếu
# print(df.isna())

# 2.Loại bỏ dữ liệu khuyết thiếu
df1 = df.dropna()

# 3. % số lượng bản ghi còn lại
# print(100 * df1.shape[0]/df.shape[0])

# 4. vẽ biểu đồ phân bố
# sns.kdeplot(data=df1['MonthlyIncome'])
# plt.show()

# Các đặc trưng đều là giá trị liên tục nên ta sẽ áp dụng 
# phương pháp thay thế nội suy
# 5. thay thế dữ liệu khuyết thiếu bởi giá trị nội suy theo cột
df2 = df.interpolate(axis=1)

# ---- Xử lý dữ liệu ngoại lai -----

# 1. vẽ biểu đồ boxplot cho các đặc trưng
# df2.boxplot()
# plt.show()

# 2. vẽ biểu đồ box plot cho MonthlyIncome
# sns.boxplot(df2['MonthlyIncome'])
# plt.show()

# 3. tính giá trị Q1 và Q3
Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)

# 4. tính IQR
IQR = Q3 - Q1

# 5. lọc dữ liệu ngoại lai
df3 = df2[~((df2 < (Q1 - 1.5*IQR)) | (df2 > (Q3 + 1.5*IQR))).any(axis=1)]
# df3.boxplot()
# plt.show()

# sns.boxplot(df3['MonthlyIncome'])
# plt.show()

# ----- Chuẩn hóa dữ liệu -------
# chuẩn hóa trên cột MonthlyIncome
# phân bố dữ liệu trên cột MonthlyIncome
# sns.kdeplot(data=df3['MonthlyIncome'])
# plt.show()

# -------- 1. Chuẩn hóa với minmax scaling
scaler = MinMaxScaler()
mms = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
sns.kdeplot(data=mms)
plt.show()

# -------- 2. Chuẩn hóa với robust scaling
scaler_robust = RobustScaler()
rbs = scaler_robust.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
sns.kdeplot(data=rbs)
plt.show()

# -------- 3. Chuẩn hóa với standard scaling
scaler_standard = StandardScaler()
sc = scaler_standard.fit_transform(pd.DataFrame(df3['MonthlyIncome']))
sns.kdeplot(data=sc)
plt.show()