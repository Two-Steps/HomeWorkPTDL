import mysql.connector
from mysql.connector import errorcode
import pandas as pd

cnx = mysql.connector.connect(user='hocvien', password='CodeGym',
                              host='14.225.44.220',
                              database='classicmodels')
is_connected = cnx.is_connected()
print(f'connect to my sql successfully: {is_connected}')

# viet truy van
# b1: create cursor
executor = cnx.cursor()
# b2: query
query = 'SELECT * FROM employees '
# 7. lay ra top3 best saler
query7 = "select e.employeeNumber, SUM(p.amount) as totalsale from employees e left join customers c on e.employeeNumber = c.salesRepEmployeeNumber left join payments p on c.customerNumber = p.customerNumber GROUP by e.employeeNumber ORDER  by totalsale DESC limit 3"
# 8. thống kê doanh số theo tháng
query8 = ""
# 10. lay ra nhan vien cu the thỏa mãn ở tỉnh A và bán hàng ở  tỉnh khác, hỏi hàng là doangh theo tỉnh ntn??
query10 = ""
# 11 CRM: tính ra % độ trễ giao hàng vs top_k khách hàng vip(mua hàng có payment lớn nhất) theo từng thành phố
query11 = "select e.employeeNumber , o.city as 'office city', c.city as 'other city',  SUM(p.amount)\
    from offices o inner join employees e on o.officeCode = e.officeCode \
    inner join customers c on e.employeeNumber = c.salesRepEmployeeNumber  \
    inner join payments p on c.customerNumber = p.customerNumber \
    GROUP by e.employeeNumber , o.city, c.city"
# run
executor.execute(query11)
# for data in executor:
#     print(data)
result = executor.fetchall()
column_names = [i[0] for i in executor.description]
# print(result)
# export csv
df = pd.DataFrame(result, columns=column_names)
print(df.head())



# try:
#     connection = mysql.connector.connect(host='14.225.44.220',
#                                         database= "classicmodels",
#                                         user="hocvien",
#                                         password="CodeGym")
                                        
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor() # open new sql scrip
#         # tip 
#         cmd = "select * from products p  where p.productCode  in \
#             (select DISTINCT(o2.productCode)  from orders o left join orderdetails o2 on o.orderNumber =o2.orderNumber\
#               where o.customerNumber =141)"
#         cursor.execute(cmd)
#         record = cursor.fetchall()
#         field_names = [i[0] for i in cursor.description]
#         df = pd.DataFrame(record, columns=field_names)
#         print(df)
#     else:
#         print("Can not connect to DB mysql")
# except Error as e:
#     print("Error while connecting to MySQL", e)
