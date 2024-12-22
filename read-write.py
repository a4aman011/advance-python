import pymysql as p

con=p.connect(
    user='root',
    password='tiger',
    host='localhost'
)

cur=con.cursor()

cur.execute("select * from student.std_info where stream='FINANCE'")

for std in cur:
    print(std)

con.commit()
