import pymysql as p

con=p.connect(
    user='root',
    password='tiger',
    host='localhost'
)

cur=con.cursor()

# cur.execute("insert into student.std_info(usn,sname,degree,stream,marks,grade) values ('1RV19CS012','AMISH','BE','CSE',85,'A');")
query="insert into student.std_info(usn,sname,degree,stream,marks,grade) values (%s,%s,%s,%s,%s,%s)"

values=[
    ('1RV19CS013','ANKIT','BSC','CSE',55,'D'),
    ('1RV19CS014','SONU','BCOM','FINANCE',75,'B'),
    ('1RV19CS015','AMAN','BE','CSE',65,'C'),
    ('1RV19CS016','ANJALI','BSC','CSE',55,'D'),
    ('1RV19CS017','ANKIT','BSC','CSE',55,'D')
]
cur.executemany(query,values)
con.commit()
print("row inserted")