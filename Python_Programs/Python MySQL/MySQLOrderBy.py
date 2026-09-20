import mysql.connector

host=input("Host: "); user=input("Username: "); password=input("Password: "); db=input("Database: "); table=input("Table: ")
order=input("Enter ASC or DESC: ").upper()
if order not in ("ASC","DESC"): raise ValueError("Use ASC or DESC")
conn=mysql.connector.connect(host=host,user=user,password=password,database=db)
cur=conn.cursor()
cur.execute(f"SELECT * FROM `{table}` ORDER BY name {order}")
for row in cur.fetchall(): print(row)
cur.close(); conn.close()
