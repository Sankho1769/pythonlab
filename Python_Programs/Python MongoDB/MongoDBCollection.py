from pymongo import MongoClient

uri=input("Enter MongoDB URI: "); db_name=input("Database: "); collection=input("Collection: ")
client=MongoClient(uri)
db=client[db_name]
if collection not in db.list_collection_names(): db.create_collection(collection)
print("Collection ready:", collection)
client.close()
