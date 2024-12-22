import pymysql as p

try:
    con=p.connect(
        user='root',
        password='tiger',
        host='localhost'
    )

    cur=con.cursor()

    # cur.execute("create database student")
    cur.execute("create table student.std_info( USN varchar(10), SNAME varchar(20), DEGREE varchar(20), STREAM varchar(20), MARKS int(10), GRADE varchar(5))")
    print("table created")
    # for db in cur:
    #     print(db)

except Exception as e:
    print(e)

