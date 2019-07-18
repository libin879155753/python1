import pymysql
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                    password='123456',
                    database='stu',
                    charset='utf8')

cur=db.cursor()
# 执行sql语句
# sql="update interest set price=9600 where name='lol'; "
sql="delete from class1 where score=0;"
cur.execute(sql)
db.commit()
cur.close()
db.close()