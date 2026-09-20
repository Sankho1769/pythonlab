import mysql.connector

host=input("Host: "); user=input("Username: "); password=input("Password: "); db=input("Database: "); table=input("Table: ")
id_value=int(input("ID to update: ")); name=input("New name: "); age=int(input("New age: "))
conn=mysql.connector.connect(host=host,user=user,password=password,database=db)
cur=conn.cursor()
cur.execute(f"UPDATE `{table}` SET name=%s, age=%s WHERE id=%s",(name,age,id_value))
conn.commit()
print("Updated rows:", cur.rowcount)
cur.close(); conn.close()
