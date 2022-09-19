# Thực hành rời rạc hóa các biến định lượng
import pandas as pd
import numpy as np

# Giả sử ta có dữ liệu về một nhóm người trong một nghiên cứu và 
# muốn nhóm họ thành các nhóm tuổi riêng biệt
ages = [20, 92, 95, 97, 21, 23, 37, 31, 61, 45, 41, 32]
# Hãy chia chúng thành các nhóm từ 18 đến 25, 26 đến 35, 36 đến 60 và cuối cùng là 61 trở lên.
# Để làm như vậy, chúng ta phải sử dụng cut trong pandas

# Định nghĩa khoảng giá trị các nhóm
bins = [18, 25, 35, 60, 100]
# Rời rạc hóa
cats = pd.cut(ages, bins)
# print(cats)
# Lấy ra index của nhóm tương ứng với các phần tử
print(cats.codes)
# Lấy ra các nhóm
print(cats.categories)
# Thống kê số lượng phần tử mỗi nhóm
print(pd.value_counts(cats))
# * Khi truyền tham số right = False, ta thay đổi các lấy ngưỡng 
# giá trị vd: (18, 25] thành [18, 25)
cats2 = pd.cut(ages, bins, right=False)
# print('cats2: ',cats2)
# * Ta cũng có thể chuyển tên các nhóm của riêng mình vào một danh sách
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# print(pd.cut(ages, bins, labels=group_names))

# sinh dữ liệu ngẫu nhiên gồm 20 phần tử
# data = np.random.rand(20)
# Tùy chọn precision = 2 sẽ giới hạn độ chính xác thập phân ở hai chữ số.
# cut_data = pd.cut(data, 4, precision=2)

# --------------Nótè-----------
#   -Hàm cut sẽ chia dữ liệu thành các khoảng bins, hoặc tự động 
#    nhưng các khoảng sẽ bằng nhau
#   -Hàm qcut sẽ chia dữ liệu thành các khoảng có số lượng phần 
#    tử trong mỗi khoảng bằng nhau

 # sinh ngẫu nhiễn 1000 điểm dữ liệu
data = np.random.randn(1000)
# thực hiện hàm qcut trên dữ liệu vừa sinh ra
cats3 = pd.qcut(data, 4)
#thống kê số lượng phần tử
print(pd.value_counts(cats3))
cats4 = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
print('cats4', cats4)
print(pd.value_counts(cats4))