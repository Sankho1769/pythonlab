import mysql.connector

host=input("Host: "); user=input("Username: "); password=input("Password: "); db=input("Database: "); table=input("Table: ")
limit=int(input("Number of records: "))
conn=mysql.connector.connect(host=host,user=user,password=password,database=db)
cur=conn.cursor()
cur.execute(f"SELECT * FROM `{table}` LIMIT %s",(limit,))
for row in cur.fetchall(): print(row)
cur.close(); conn.close()
