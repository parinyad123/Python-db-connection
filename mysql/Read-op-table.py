import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="123qaz",
                             database="harshdb")

mycursor=mydb.cursor()

# เลือกคนแรก17
# mycursor.execute("select name from employee")
# myresult=mycursor.fetchone()

# เลือกทั้งหมด
mycursor.execute("Select * from employee")
myresult=mycursor.fetchall()

for row in myresult:
    print(row)

# run in sql >> select name from employee;
