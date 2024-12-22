import pymysql as p

con=p.connect(
    user='root',
    password='tiger',
    host='localhost'
)

cur=con.cursor()
try:
    cur.execute("create database userdata")
    print('database created')
    try:
        cur.execute("create table userdata.user_info(name varchar(20), age int(10), phone int(10), address varchar(50))")
        print('table created')
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            phone = (int(input("Enter phone number: ")))
            address = input("Enter address: ")

            query= "insert into userdata.user_info(name,age,phone,address) values (%s,%s,%s,%s)"
            values=[name,age,phone,address]

            cur.execute(query,values)
            con.commit()
            print('data is inserted')
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)



