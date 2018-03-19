from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

#print(db.collection_names())

new_post ={
"title":"Thắc mắc",
"author":"A bờ cờ",
"content": "Tòa nhà Techkids có thang thoát hiểm ko?",
}

db.posts.insert_one(new_post)
