import mysql.connector

host=input("Host: "); user=input("Username: "); password=input("Password: "); db=input("Database: ")
table1=input("First table: "); table2=input("Second table: ")
conn=mysql.connector.connect(host=host,user=user,password=password,database=db)
cur=conn.cursor()
cur.execute(f"SELECT * FROM `{table1}` JOIN `{table2}` ON `{table1}`.id=`{table2}`.id")
for row in cur.fetchall(): print(row)
cur.close(); conn.close()
