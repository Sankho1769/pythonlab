from pymongo import MongoClient

uri=input("URI: "); db_name=input("Database: "); collection=input("Collection: ")
client=MongoClient(uri)
client[db_name][collection].drop()
print("Collection dropped.")
client.close()
