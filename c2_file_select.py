from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db_name = 'db_crawl_data_ver2'
db = client[db_name]

collection_name = 'crawl'
collection = db[collection_name]

pipeline = [
    {"$sort": {"ID": 1, "time": 1}}
]
sorted_collection = collection.aggregate(pipeline)
for document in sorted_collection:
    print(document)