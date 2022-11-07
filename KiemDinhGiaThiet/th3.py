# Bộ phận bán hàng của Công ty Coca Cola tuyên bố rằng lượng tiêu thụ coca trung
# bình ở Ohio lớn hơn ở Atlanta. Để tiến hành chiến lược phân phối sản phẩm ở 
# 2 khu vực này, bộ phận Marketing có thu thập số liệu sử dụng coca của 50 
# người ở Ohio và 50 người ở Atlanta. Dữ liệu được để trong file Coca_cola_use.xlsx,
# với đơn vị tiêu thụ được tính l/năm cho 1 người. Với mức ý nghĩa 5% hãy kiểm
# định giả thuyết xem có đúng lượng tiêu thụ Coca bình quân ở Ohio lớn hơn Atlanta hay không.

import pandas as pd
from scipy import  stats
import matplotlib.pyplot as plt

df = pd.read_excel("Coca_cola_use.xlsx", index_col= 'STT')
print(df.head())
print(df.info())
print(df.describe())
df.boxplot()
# plt.show()
# Thực hiện kiểm định giả thuyết so sánh hai mẫu trung bình độc lập 
# gọi a1, a2 lần lượt là lượng tiêu thụ coca trung bình trên đầu người ở Ohio và Atlanta
# Giả thuyết không: a1-a2 =0
# Giả thuyết đối: a1-a2>0
# mức ý nghĩa 5%
# **Loại kiểm định Independent T test
print (stats.ttest_ind(df.Ohio, df.Atlanta,equal_var=False))
# Chúng ta nhìn thấy rằng: pvalue = 0.541 > 5% rất nhiều nên không đủ cơ sở để bác bỏ 
# giả thuyết không 
# Kết luận: Không đủ căn cứ để kết luận rằng lượng tiêu thụ coca trung bình ở 
# Ohio lớn hơn ở Atlanta