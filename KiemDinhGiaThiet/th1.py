import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('FoodPrice_in_Turkey.csv')
df.info()

# 1. với mức ý nghĩa 5% kiểm định giả thuyết giá bán gạo trung bình 
# năm 2019 là 10 Lira/kg

# 
product_names = list(df['ProductName'].unique())
#
df_rice = df.loc[(df.ProductName == 'Rice - Retail') & (df.Year == 2019)]
print(df_rice.shape[0])
# 
df_rice['Price'].hist()
# plt.show()
# Do phân bố có xu hướng gần giống phân bố chuẩn, nên lựa chọn thực hiện kiểm định 
# 2 phía với one sample T test ?? nhìn biểu đồ :)) wtf
# Giả thuyết không: Giá gạo trung bình = 9.5
# Giả thuyết đối: Giá gạo trung bình # 9.5

print(stats.ttest_1samp(df_rice['Price'], 9.5))
# Giá trị pvalue >5% nên không đủ cơ sở để để bác bỏ giả thuyết không
# Kết luận: Với mức ý nghĩa 5% có thể nhận định giá gạo trung bình bằng 9.5 Lira/kg

# 2. Với mức ý nghĩa 5% hãy kiểm định giả thuyết: Giá bột mỳ và giá gạo ở Turkey 
# năm 2019 là bằng nhau
df_wheat = df.loc[(df.ProductName== 'Wheat flour - Retail') & (df.Year == 2019)]
# Tạo boxplot so sánh phân bố của bột mỳ vào gao
price = {'rice': list(df_rice["Price"]), 'wheat': list(df_wheat['Price'])}
df_price = pd.DataFrame(price)
# sns.boxplot(data=df_price)
# plt.show()
# Nhìn vào phân bố trên chúng ta cũng có thể kết luận được luôn, giá của bột mì
# thấp hơn hẳn giá của gạo. Để chứng minh nhận định rằng giá bột mỳ và giá gạo
# không giống nhau, chúng ta thực hiện so sánh trung bình độc lập 
# – independent T test 
# Giả thuyết không: giá bột mỳ trung bình bằng giá gạo 
# Giả thuyết đối: giá bột mỳ trung bình khác giá gạo
print(stats.ttest_ind(price['rice'], price['wheat'], equal_var=False))
# pvalue = 7.11 * 10^-55 < 5% nên bác bỏ giả thuyết không
# chấp nhận giả thuyết đối
# => giá bột mỳ và giá gạo là khác nhau trong năm 2019

# 3. Vẽ biểu đồ sự biến đổi giá gạo trung bình từ năm 1/2014 đến năm 
# 1/2019 và tìm mối liên hệ giữa giá Trà và giá Cà phê

# chuyển đổi dữ liệu ngày tháng
df['time'] =  pd.to_datetime(df['Year'].astype(str) + '/'+df['Month'].astype(str))
# thực hiện tính toán và vẽ giá trà, caffe theo tháng
df_Tea_all = df.loc[(df.ProductName == 'Tea - Retail')]
df_Tea_all_mean_by_month = df_Tea_all.groupby('time')['Price'].mean()
plt.plot_date(df_Tea_all_mean_by_month.index, df_Tea_all_mean_by_month.values, linestyle ='solid')

df_Coffee_all = df.loc[(df.ProductName == 'Coffee - Retail')]
df_Coffee_all_mean_by_month = df_Coffee_all.groupby('time')['Price'].mean()
plt.plot_date(df_Coffee_all_mean_by_month.index, df_Coffee_all_mean_by_month.values, linestyle ='solid')
# plt.show()

# Tiền xử lý dữ liệu
# Tạo một data frame thông tin gồm chứa time - place, giá trà, giá cafe
df_tea_and_coffee = df.loc[(df.ProductName.isin(['Tea - Retail','Coffee - Retail']))]

df_tea_and_coffee['time-place'] = df_tea_and_coffee['time'].astype(str) +'-'+df_tea_and_coffee['Place']
df1 = df_tea_and_coffee[df_tea_and_coffee.ProductName =='Tea - Retail'].filter(['time-place',  'Price'])
df1 = df1.rename(columns = {'Price':'Tea - Retail'})

df2 = df_tea_and_coffee[df_tea_and_coffee.ProductName =='Coffee - Retail'].filter(['time-place', 'Price'])
df2 = df2.rename(columns = {'Price':'Coffee - Retail'})

Processed_data = pd.merge(df1, df2, on = 'time-place')
print(Processed_data.head())

# Tiến hành kiểm định: Thực hiện kiểm định wilcoxon 1 phía với giả thuyết như sau
# Giả thuyết không: giá cà phê bằng giá trà công thêm 15 Lira ở mọi thời điểm
# Giả thuyết đối: Giá giá cà phê luôn hơn giá trà 15 Lira ở mọi thời điểm

# thực hiện biến đổi dữ liệu
d = Processed_data['Coffee - Retail']-Processed_data['Tea - Retail'] - 15
# Thực hiện kiểm định wilcolxon

# thực hiện kiểm định với giả thuyết đối được định nghĩa ở trên
print(stats.wilcoxon(d, alternative='greater'))
# Do pvalue <1% rất nhiều 
# –> Bác bỏ giả thuyết không, chấp nhận giả thuyết đối 
# Giá Cà phê luôn lớn hơn giá trà ít nhất 15 lira mà không bị ảnh hưởng bởi 
# thời gian hay địa điểm