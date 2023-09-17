#插入数据

import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', passwd='root', database='python', charset='utf8')

try:
   with conn.cursor() as cursor:
     affected_rows = cursor.execute('insert into students values(%s,%s,%s)',(no,name,score))  
     if affected_rows == 1:
        print("插入成功")
   conn.commit()
except pymysql.MySQLError as error:      
   print(error)
   conn.rollback()
finally:
   conn.close()
   
#删除数据
import pymysql
no = int(input('部门编号: '))

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', passwd='root', database='python', charset='utf8') 

try:
    with conn.cursor() as cursor:
      affected_rows = cursor.execute('delete from students where no=%s',(no))  
      if affected_rows == 1:
          print("删除成功")
    conn.commit()
except pymysql.MySQLError as error:
    print(error)
    conn.rollback()
finally:
    conn.close()

      
#更新数据
import pymysql
no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                      user='root', passwd='root', database='python', charset='utf8')

try:
    with conn.cursor() as cursor:
      affected_rows = cursor.execute('update students set name=%s,location=%s where no=%s',(name,location,no))  
      if affected_rows == 1:
          print("更新成功")

    conn.commit() 
except pymysql.MySQLError as error:
    print(error)
    conn.rollback()
finally:
    conn.close()
    
    
    
#查询数据
import pymysql

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', passwd='root', database='python', charset='utf8')

try:
    with conn.cursor() as cursor:
        cursor.execute('select * from students')
        for row in cursor.fetchall():
            print(row)
                    
except pymysql.MySQLError as error:
    print(error)
finally:
    conn.close()
    
#分页查询
import pymysql
page = int(input('页码: '))
size = int(input('大小: '))

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                      user='root', passwd='root', database='python', charset='utf8')

try:
    with conn.cursor() as cursor:
        cursor.execute('select * from students limit %s,%s',((page-1)*size,size))
        for row in cursor.fetchall():
            print(row)
except pymysql.MySQLError as error:
    print(error)  
finally:
  conn.close()
  
     
  
import openpyxl
import pymysql

# 创建工作簿对象
workbook = openpyxl.Workbook()
# 获得默认的工作表
sheet = workbook.active
# 修改工作表的标题
sheet.title = '员工基本信息'
# 给工作表添加表头
sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))
# 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4')
try:
    # 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 通过游标对象执行SQL语句
        cursor.execute(
            'select `eno`, `ename`, `job`, `sal`, coalesce(`comm`, 0), `dname` '
            'from `tb_emp` natural join `tb_dept`'
        )
        # 通过游标抓取数据
        row = cursor.fetchone()
        while row:
            # 将数据逐行写入工作表中
            sheet.append(row)
            row = cursor.fetchone()
    # 保存工作簿
    workbook.save('hrs.xlsx')
except pymysql.MySQLError as err:
    print(err)
finally:
    # 关闭连接释放资源
    conn.close()                         