import pymysql
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                    password='123456',
                    database='stu',
                    charset='utf8')

cur=db.cursor()
# 执行sql语句
sql="insert into class1 values (9,'雨天',17,'w',76.5,'2019-8-7');"

cur.execute(sql)
db.commit()
cur.close()
db.close()
print("djuioru  wkleur0n")
