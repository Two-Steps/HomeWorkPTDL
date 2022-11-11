import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('GDPlist.csv', encoding='latin1')
print(df.head())
# 1 Trung bình GDP của các quốc gia trên thế giới là 500 tỉ usd/năm
print(stats.ttest_1samp(df['GDP (millions of US$)'], 500000))
#Ttest_1sampResult(statistic=0.3757438669518338, pvalue=0.7077493494055246)
# pvalue > 5% (tự lấy mốc 5%) nên H0 là đúng, gdp tb của tg là 500 tỉ đô/năm

# 2 GDP trung bình của các quốc gia ở châu Âu và châu Mỹ là bằng nhau
gr = df.groupby('Continent')['GDP (millions of US$)'].mean()
# print(gr.iloc[2]) -- châu âu
# print(gr.iloc[3, ]) -- mỹ
print(stats.ttest_rel(gr.iloc[2], gr.iloc[3]))
# bác bỏ H0