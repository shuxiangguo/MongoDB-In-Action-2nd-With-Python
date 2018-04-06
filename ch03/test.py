from pymongo import MongoClient
import pprint
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017')

db = client.tutorial
db_coll = db["users"]

smith = {"last_name": "smith", "age": 30}
jones = {"last_name": "jones", "age": 40}
smith_id = db_coll.insert_one(smith).inserted_id
jones_id = db_coll.insert_one(jones).inserted_id

pprint.pprint(db_coll.find_one({"last_name": "smith"}))
print(db_coll.count())

# # update and delete
# db_coll.find({"last_name": "smith"}).update_one(
# 				{"$set": {"city": "Chicago"}})

db_coll.find({"last_name": "smith"}).delete_one