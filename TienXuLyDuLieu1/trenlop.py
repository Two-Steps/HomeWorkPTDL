import numpy as np

import seaborn
from matplotlib import pyplot as plt
from scipy import stats

data = [80,71,79,61,78,73,77,74,76,75,160,79,80,78,75,78,86,80,82,69,100,72,74,75,180,72,71,12]

# bien doi z_score
z_score = stats.zscore(data)
print(z_score)

# bien doi ve array de dung cac bieu thuc logic cua numpy
z_score = np.array(z_score)
data = np.array(data)

# viet expression logic
logic = (z_score >-0.3) & (z_score < 0.5)
print()
print(z_score[logic])
# lay du lieu
print(data[logic])