import mysql.connector

host=input("Host: "); user=input("Username: "); password=input("Password: "); db=input("Database: "); table=input("Table: ")
name=input("Name to search: ")
conn=mysql.connector.connect(host=host,user=user,password=password,database=db)
cur=conn.cursor()
cur.execute(f"SELECT * FROM `{table}` WHERE name=%s",(name,))
for row in cur.fetchall(): print(row)
cur.close(); conn.close()
