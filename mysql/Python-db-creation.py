import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", passwd="123qaz")

print(mydb)

if(mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccessful")