import pymysql
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                    password='123456',
                    database='stu',
                    charset='utf8')

cur=db.cursor()
# 执行sql语句
# try:
#     name=input("name:")
#     age=int(input("age:"))
#     score=float(input("score:"))

try:
    name=input("name:")
    age=input("age:")
    score=input("score:")
    # sql='insert into class1 (name,age,score) values ("%s",%d,%f);'%(name,age,score)
    sql = 'insert into class1 (name,age,score) values (%s,%s,%s);'
    # cur.execute(sql)
    cur.execute(sql,[name,age,score])

    db.commit()
except Exception as e:
    db.rollback()
    print(e)
cur.close()
db.close()



