import pymysql
import re
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                    password='123456',
                    database='dict',
                    charset='utf8')

cur=db.cursor()
# 执行sql语句
with open("dict.txt") as f:
    data=f.readline()
    tep=data.split(" ")
    单词=tep[0]
    解释=' '.join(tep[1:]).strip()
    sql="insert into words (单词,解释) values (%s,%s)"


# f= open("dict.txt")
# sql="insert into words (单词,解释) values (%s,%s)"
# for line in f:
#     tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    try:
        cur.execute(sql,[单词,解释])
        db.commit()
    except:
        db.rollback()
f.close()
cur.close()
db.close()
