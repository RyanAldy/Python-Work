import pymysql

db = pymysql.connect("localhost", "root", "", "ryantest")
c = db.cursor()
#c.execute("insert into emp values(3, 'The shafeeq', 40)")
c.execute("select * from emp")
return_all = c.fetchall()
db.commit()

for record in return_all:
    print(record)
