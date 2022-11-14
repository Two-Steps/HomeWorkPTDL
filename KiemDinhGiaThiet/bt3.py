import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('Credit_Scoring.csv')
df = df.dropna()
print(df.describe())
# Có phải những khách hàng không có người phụ thuộc sẽ có thu nhập trung bình theo tháng (MonthlyIncome) nhỏ hơn những khách hàng 
# có người phụ thuộc không (với mức ý nghĩa 10%)
df_depen = df[df['NumberOfDependents'] > 0]
# print(df_depen['MonthlyIncome'])
df_no_depen = df[df['NumberOfDependents'] == 0]
# print(df_no_depen['MonthlyIncome'])
# print(stats.ttest_ind(df_depen['MonthlyIncome'], df_no_depen['MonthlyIncome']))
# => cháp nhận H1

# Có phải trung bình số lượng khoản vay (NumberOfOpenCreditLinesAndLoans) những khách hàng gặp khó khăn trong vòng 2 năm trở lại đây (SeriousDlqin2yrs =1) 
# thì sẽ cao hơn những khách hàng không gặp khó khăn không với mức ý nghĩa 10%
oce1 = df[df['SeriousDlqin2yrs'] == 1]['NumberOfOpenCreditLinesAndLoans']
oce2 = df[df['SeriousDlqin2yrs'] == 0]['NumberOfOpenCreditLinesAndLoans']

print(stats.ttest_ind(oce1, oce2))
# => cháp nhận H1