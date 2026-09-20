from pymongo import MongoClient

uri=input("URI: "); db_name=input("Database: "); collection=input("Collection: ")
direction=input("Sort direction (asc/desc): ").lower()
direction = 1 if direction=="asc" else -1
client=MongoClient(uri)
for doc in client[db_name][collection].find().sort("name",direction): print(doc)
client.close()
