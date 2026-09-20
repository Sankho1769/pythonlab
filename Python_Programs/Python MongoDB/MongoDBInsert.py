from pymongo import MongoClient

uri=input("URI: "); db_name=input("Database: "); collection=input("Collection: ")
name=input("Name: "); age=int(input("Age: "))
client=MongoClient(uri)
result=client[db_name][collection].insert_one({"name":name,"age":age})
print("Inserted ID:", result.inserted_id)
client.close()
