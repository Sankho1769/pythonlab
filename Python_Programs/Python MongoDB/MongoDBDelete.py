from pymongo import MongoClient

uri=input("URI: "); db_name=input("Database: "); collection=input("Collection: ")
name=input("Name to delete: ")
client=MongoClient(uri)
result=client[db_name][collection].delete_many({"name":name})
print("Deleted:", result.deleted_count)
client.close()
