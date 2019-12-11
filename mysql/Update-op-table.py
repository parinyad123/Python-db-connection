import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="123qaz",
                             database="harshdb")

mycursor=mydb.cursor()

sql="UPDATE employee SET salary=70000 WHERE name='ankita'"
mycursor.execute(sql)

mydb.commit()


########################################################################
#############  Show employee  ( Read-op-table.py )####################
mycursor.execute("Select * from employee")
myresult=mycursor.fetchall()

for row in myresult:
    print(row)
#######################################################################