import mysql.connector

host=input("Host: "); user=input("Username: "); password=input("Password: "); db=input("Database: "); table=input("Table: ")
id_value=int(input("ID to delete: "))
conn=mysql.connector.connect(host=host,user=user,password=password,database=db)
cur=conn.cursor()
cur.execute(f"DELETE FROM `{table}` WHERE id=%s",(id_value,))
conn.commit()
print("Deleted rows:", cur.rowcount)
cur.close(); conn.close()
