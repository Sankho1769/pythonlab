from pymongo import MongoClient

uri = input("Enter MongoDB connection URI: ")
client = MongoClient(uri)
print("Connected to MongoDB.")
client.close()
