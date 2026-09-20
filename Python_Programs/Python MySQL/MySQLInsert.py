import mysql.connector

host=input("Host: "); user=input("Username: "); password=input("Password: "); db=input("Database: "); table=input("Table: ")
name=input("Student name: "); age=int(input("Student age: "))
conn=mysql.connector.connect(host=host,user=user,password=password,database=db)
cur=conn.cursor()
cur.execute(f"INSERT INTO `{table}` (name,age) VALUES (%s,%s)",(name,age))
conn.commit()
print("Inserted.")
cur.close(); conn.close()
