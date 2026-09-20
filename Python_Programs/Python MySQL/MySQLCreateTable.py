import mysql.connector

host = input("Enter MySQL host: ")
user = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")
db = input("Enter database name: ")
table = input("Enter table name: ")

conn = mysql.connector.connect(host=host, user=user, password=password, database=db)
cursor = conn.cursor()
cursor.execute(f"CREATE TABLE `{table}` (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT)")
print("Table created.")
cursor.close()
conn.close()
