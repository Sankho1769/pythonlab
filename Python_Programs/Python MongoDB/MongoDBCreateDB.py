from pymongo import MongoClient

uri=input("Enter MongoDB connection URI: "); db_name=input("Enter database name: ")
client=MongoClient(uri)
db=client[db_name]
db.create_collection("temporary") if "temporary" not in db.list_collection_names() else None
print("Database selected:", db.name)
client.close()
