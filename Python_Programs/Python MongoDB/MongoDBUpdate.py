from pymongo import MongoClient

uri=input("URI: "); db_name=input("Database: "); collection=input("Collection: ")
name=input("Name to update: "); new_age=int(input("New age: "))
client=MongoClient(uri)
result=client[db_name][collection].update_many({"name":name},{"$set":{"age":new_age}})
print("Updated:", result.modified_count)
client.close()
