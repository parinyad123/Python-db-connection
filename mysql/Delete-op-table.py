import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="123qaz",
                             database="harshdb")

mycursor=mydb.cursor()

sql="DELETE FROM employee WHERE name='harshit'"

mycursor.execute(sql)

mydb.commit()

########################################################################
#############  Show employee  ( Read-op-table.py )####################
mycursor.execute("Select * from employee")
myresult=mycursor.fetchall()

for row in myresult:
    print(row)
#######################################################################