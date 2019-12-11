import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root", password="123qaz")

mycursor=mydb.cursor()
mycursor.execute("Create table employee(name varchar(200), sal int(20))")