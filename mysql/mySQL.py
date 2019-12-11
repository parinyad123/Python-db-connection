import pyodbc

#con_string='driver=MySQL ODBC 8.0 Unicode Driver;server=172.27.106.200;database=testdb;uid=test1,pwd=test123'
con_string='driver=MySQL ODBC 8.0 Unicode Driver;server=localhost:3306;database=testdb;uid=test1,pwd=test123'

def create_table():
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
            create table perosn(
                id int PRO=IMARY KEY AUTO_INCREMENT,
                gender char(1),
                weight float,
                height float
            )
        """
        con.execute(sql_cmd)

if __name__=='__main__':
    create_table