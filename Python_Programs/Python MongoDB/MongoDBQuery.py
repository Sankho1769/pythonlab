from pymongo import MongoClient

uri=input("URI: "); db_name=input("Database: "); collection=input("Collection: ")
name=input("Name to search: ")
client=MongoClient(uri)
for doc in client[db_name][collection].find({"name":name}): print(doc)
client.close()
