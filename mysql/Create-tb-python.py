import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="123qaz",
                             database="harshdb")

mycursor=mydb.cursor()

# Create table of database harshdb
#mycursor.execute("Create table employee(name varchar(200), salary int(20))")

mycursor.execute("show tables")

for tb in mycursor:
    print(tb)

# run in sql >> describe employee;