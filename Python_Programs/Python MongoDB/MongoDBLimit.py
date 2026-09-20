from pymongo import MongoClient

uri=input("URI: "); db_name=input("Database: "); collection=input("Collection: ")
limit=int(input("Number of documents: "))
client=MongoClient(uri)
for doc in client[db_name][collection].find().limit(limit): print(doc)
client.close()
