import mysql.connector

host = input("Enter MySQL host: ")
user = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")
db = input("Enter database name: ")

conn = mysql.connector.connect(host=host, user=user, password=password)
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE `{db}`")
print("Database created.")
cursor.close()
conn.close()
