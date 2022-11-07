import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


# tao du lieu
data1 = np.random.normal(0,0.1,100)
data2 = np.random.normal(0,0.1,100)

# ti distribution => f(x) , f(y)
kde1 = gaussian_kde(data1,bw_method=0.2)
kde2 = gaussian_kde(data2,bw_method=0.2)

# tim diem cuc tieu, cuc dai ma la giao nhau cua 2 distribution do.
x_min = min(data1.min(), data2.min())
x_max = min(data1.max(), data2.max())

# tao dx
dx = 0.2 *(x_max - x_min)
x_min -=dx
x_max +=dx


# tao ramdom du lu lieu trong khoang tu xmi, x_max 
x = np.linspace(x_min, x_max, 500)


kde_new_1 = kde1(x)
kde_new_2 = kde2(x)

# distribition
x_area_interaction = np.minimum(kde_new_1, kde_new_2)

# tinh toan dien tich . tich phan
percent = np.trapz(x_area_interaction, x )

percent = np.round(percent * 100,2)

plt.plot(x, kde_new_1, color="b", label='abc')
plt.fill_between(x,kde_new_1,0, color="b", alpha = 0.2)

plt.plot(x, kde_new_2, color="orange", label='xyz')
plt.fill_between(x,kde_new_2,0, color="orange", alpha = 0.2)

#plot phan giao nhau bang mau gi do(red)
plt.plot(x, x_area_interaction, color="r", label='interaction')
plt.fill_between(x,kde_new_2,0, color="r", alpha = 0.2)

handles, labels = plt.gca().get_legend_handles_labels()
labels[2] += f": {percent} %"
plt.legend(handles, labels)
plt.show()