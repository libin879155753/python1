"""
二进制存头像
"""
import pymysql
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                    password='123456',
                    database='stu',
                    charset='utf8')

cur=db.cursor()
with open("image.jpg","rb") as f:
    data=f.read()
    try:
        sql="update stu set image=%s where name='张三';"
        cur.execute(sql,[data])
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)


p=open("hu.jpg",'rb')
try:
    sql="select name from class1 where image='image.jpg';"
    p.write()


cur.close()
db.close()