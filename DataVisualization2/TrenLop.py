from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# y1 = np.random.normal(200, 30, size = 100)
# y2 = np.random.normal(100,70, size = 100)
# data = pd.DataFrame({'y1': y1, 'y2': y2, 'index': pd.date_range('1/1/2021',
# periods=100)})
# #Vẽ đồ thị ghép (cùng loại trên cùng 1 axes)
# plt.plot(data.index, data.loc[:,'y1'], 'r', label='y1') #Đường y1 màu đỏ
# plt.plot(data.index, data.loc[:,'y2'], 'b', label='y2') #Đường y2 màu xanh

# plt.title('Đồ thị phân bố normal') #Tên đồ thị
# plt.xlabel('Index') #Tên trục X
# plt.ylabel('Dao động') #Tên trục Y
# plt.legend() #Legend (chỉ nên dùng khi có từ 2 đồ thị con trở lên)
# plt.show()

#Tạo dữ liệu nhân tạo
y3 = np.random.normal(200, 30, size = 100)
y4 = np.random.normal(1000, 200, size = 100)
data = pd.DataFrame({'y3': y3, 'y4': y4, 'date': pd.date_range('1/1/2021', periods=100)})
print(data.head(10))
plt.plot(data.index, data.loc[:, 'y3'], 'r', label= 'y3')
plt.plot(data.index, data.loc[:, 'y4'], 'b', label= 'y4')
plt.title('Đồ thị phân bố normal')
plt.xlabel('Index')
plt.ylabel('Dao động')
plt.legend()
plt.show()
# => nên tránh vẽ khi 2 scale cách biệt lớn thế này
# sẽ gây hiểu làm dữ liệu

#Tạo dữ liệu nhân tạo
y1 = np.random.normal(100, 30, size = 100)
y2 = np.random.normal(100, 70, size = 100)
y3 = np.random.normal(200, 30, size = 100)
y4 = np.random.normal(1000, 200, size = 100)
data2 = pd.DataFrame({'y1':y1, 'y2':y2, 'y3': y3, 'y4': y4})

#Tạo Figure và Subplot (các axes = ax)
fig1, ax = plt.subplots(3,1)
ax[0].plot(data2['x'], data2['y1'], label='y1')
ax[1].plot(data2['x'], data2['y2'], label='y2')
ax[2].plot(data2['x'], data2['y3'], label='y3')

ax[0].set_title('Giá các mặt hàng')
ax[2].set_xlabel('Ngày')
ax[1].set_ylabel('Giá trị dầu')
ax[0].set_ylabel('Giá vàng')
ax[2].set_ylabel('Giá đôla')

ax[0].set_xticklabels([])
ax[1].set_xticklabels([])

ax[0].tick_params(axis='y', size = 8)
ax[1].tick_params(axis='y', size = 8)
ax[2].tick_params(axis='y', size = 8)

ax[0].tick_params(axis='x', size = 0)
ax[1].tick_params(axis='x', size = 0)
ax[2].tick_params(axis='x', size = 8)

# ax[0].set_xticks([])
# ax[1].set_xticks([])


#Tạo dữ liệu nhân tạo
y1 = np.random.normal(100, 30, size = 100)
y2 = np.random.normal(100, 70, size = 100)
y3 = np.random.normal(200, 30, size = 100)
y4 = np.random.normal(1000, 200, size = 100)
data3 = pd.DataFrame({'y1':y1, 'y2':y2, 'y3': y3, 'y4': y4})
# xanh lục, xanh biển, vàng
fig2, ax = plt.subplots(2, 2, sharex=True)

ax[0][0].plot(data3.index, data3['y1'], label='y1', c='red')
ax[0][1].plot(data3.index, data3['y2'], label='y2', c='green')
ax[1][0].plot(data3.index, data3['y3'], label='y3', c='blue')
ax[1][1].plot(data3.index, data3['y4'], label='y4', c='pink')

ax[0][0].set_ylabel('y1')
ax[0][1].set_ylabel('y2')
ax[1][0].set_ylabel('y3')
ax[1][1].set_ylabel('y4')

ax[1][0].set_xlabel('My Index')
ax[1][1].set_xlabel('My Index')

#Đặt tên cho từng axes
# ax[0][0].set_title('Đây là màu đỏ')
# ax[0][1].set_title('Đây là màu lam')
# ax[1][0].set_title('Đây là màu lục')
# ax[1][1].set_title('Đây là màu hồng')

#Thêm ledend cho mỗi axes
ax[0][0].legend()
ax[0][1].legend()
ax[1][0].legend()
ax[1][1].legend()

#Đặt tên cho cả figure
plt.suptitle('Ví dụ 3')

plt.tight_layout() #Tự động căn chỉnh đồ thị cho đẹp
plt.show()

#Tạo dữ liệu
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [12.2, 16.3, 20.5, 25.4, 31.2, 14.2, 24, 19.5, 28.1, 21.7]
y2 = [2000, 4000, 1200, 3200, 5600, 2300, 3600, 2500, 3100, 3000]
plt.bar(x, y1, label = 'bar 1', width = 0.5);

axes1 = plt.gca() #get current axes -> lấy giá trị của trục vừa mới vẽ
axes2 = axes1.twinx() #Tạo trục thứ 2 chia sẻ trục X với trục axes1
axes2.plot(x,y2,label = 'line 1', linewidth = 2, c = 'r', marker = 'o')

# plt.plot(x,y2,label = 'line 1', linewidth = 2, c = 'r', marker = 'o')

plt.title('Ví dụ')
axes1.set_ylabel('Biểu đồ cột trục Y')
axes2.set_ylabel('Biểu đồ đường trục Y')
axes1.set_xlabel('Trục X')
axes1.tick_params(axis='y', colors='blue')
axes2.tick_params(axis='y', colors='red')
plt.show()

#Nhập dữ liệu
x1 = ['P1','P2','P3','P4','P5']
y1 = [12.2, 16.3, 20.5, 25.4, 31.2]
y2 = [20.3, 22.6, 31.4, 33.7, 39.2]
y3 = [16.3, 17.6, 24.4, 26.7, 33.2]
fig, ax = plt.subplots(2, 2);

ax[0][0].bar(x1, y1)
ax[0][0].set_title('Y1 cột')

ax[1][0].bar(x1, y2)
ax[1][0].set_title('Y2 cột')

ax[0][1].pie(y1, labels=x1, autopct='%1.f%%', radius=1.3)
ax[0][1].set_title('Y1 tròn')

ax[1][1].pie(y2, labels=x1, autopct='%1.f%%', radius=1.3)
ax[1][1].set_title('Y2 tròn')

plt.tight_layout()
plt.show()
