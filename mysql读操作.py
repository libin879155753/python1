import pymysql
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                    password='123456',
                    database='stu',
                    charset='utf8')
cur=db.cursor()

sql="select name,age from class1 where wm='m';"
cur.execute(sql)
# one_row=cur.fetchone()
# print(one_row)
# many_row=cur.fetchmany(4)
# print(many_row)

all_row=cur.fetchall()
print(all_row)










