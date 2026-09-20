import mysql.connector

host = input("Enter MySQL host: ")
user = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")

try:
    conn = mysql.connector.connect(host=host, user=user, password=password)
    print("Connected successfully.")
    conn.close()
except Exception as e:
    print("Connection error:", e)
