from pymongo import MongoClient

uri=input("URI: "); db_name=input("Database: "); collection=input("Collection: ")
client=MongoClient(uri)
for doc in client[db_name][collection].find(): print(doc)
client.close()
