import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root", password="123qaz")

mycursor=mydb.cursor()

# Create database "harshdb"
# mycursor.execute("Create database harshdb")

mycursor.execute("Show databases")

for db in mycursor:
    print(db)