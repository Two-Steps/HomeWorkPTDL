import pandas as pd

df = pd.read_csv('subset-covid-data.csv')
print(df.head())
print(df.info())
print(df.date.value_counts())
cleaned_data = df[df.date == '2020-04-12']
# Vẽ biểu đồ phân bố số lượng ca mắc mới ở các quốc gia
print ("trung bình số ca mắc mới: " + str(cleaned_data.cases.mean()))
print ("trung vị của số ca mắc mới: "+ str(cleaned_data.cases.median()))
import matplotlib.pyplot as plt
plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("số số ca mắc mới")
plt.ylabel("Số lượng quốc gia")
plt.show()

print("tổng số ca nhiễm và số ca ncủa các châu lục")
cleaned_data.groupby('continent')['cases','deaths'].sum()

print ("5 quốc gia có số ca nhiễm mới cao nhất")
df = df.sort_values('cases',ascending = False)
df.head(5)

print ("5 quốc gia có số ca tử vong cao nhất")
df = df.sort_values('deaths',ascending = False)
df.head(5)
