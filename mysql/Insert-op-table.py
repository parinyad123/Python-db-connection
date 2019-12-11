import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="123qaz",
                             database="harshdb")

mycursor=mydb.cursor()

sqlform="Insert into employee(name,salary) values(%s,%s)"
employees=[("harshit",20000), ("amit", 30000), ("ankita", 40000),]

# executemany() Method. This method prepares a database operation (query or command) and executes
mycursor.executemany(sqlform,employees)

mydb.commit()

# run in sql >> select*from harshdb.employee;