import pandas as pd
from scipy import  stats
# đọc bộ dữ liệu
df = pd.read_csv("subset-covid-data.csv")
print(df.describe())

# Có mối tương quan nào giữa số ca mắc và ca tử vong ở các quốc gia hay không
# Do số ca nhiễm (cases) và dân số (population) đều là thuộc tính định lượng nên sử dụng kiểm định pearson
# Giả thuyết không: Không có mối tương quan tuyến tính giữa hai biến
# Giả thuyết đối: Không có mối tương quan tuyến tính giữa hai biến
df1 = df.filter(['cases', 'population'])
# xóa bỏ dữ liệu null
df1 = df1.dropna()
r, pvalue = stats.pearsonr(df1.cases, df1.population)
print ("r: ", r, "; pvalue: ", pvalue)
# Nhận xét: do pvalue <5%, nên với mức ý nghĩa 5% bác bỏ giả thuyết không, chấp nhận giả thuyết đối

# Có mối tương quan nào giữa số ca mắc (cases) và số ca tử vong (deaths) hay không
# Do số ca nhiễm (cases) và số ca tử vong (deaths) đều là thuộc tính định lượng nên sử dụng kiểm định pearson
# Giả thuyết không: Không có mối tương quan tuyến tính giữa hai biến
# Giả thuyết đối: có mối tương quan tuyến tính giữa hai biến

df2 = df.filter(['cases', 'deaths'])
# xóa bỏ dữ liệu null
df2 = df2.dropna()
r, pvalue = stats.pearsonr(df2.cases, df2.deaths)
print ("r: ", r, "; pvalue: ", pvalue)
# Nhận xét: do pvalue ~0, nên với mức ý nghĩa 5% bác bỏ giả thuyết không, chấp nhận giả thuyết đối