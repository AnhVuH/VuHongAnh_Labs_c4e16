from pymongo import MongoClient

mongo_uri ="mongodb://admin:123456@ds117489.mlab.com:17489/aboco1"
# "mongodb://usename_db:password_db@id_of_db.mlab.com:port_of_db/aboco1"


#1. connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create Collection
games = db['games']
blogs = db['blogs']

# #4.Create a new document
# # new_game = {
# #     "name" : "Hứng bia",
# #     "description": "Best game ever"
# # }
# list_blogs = [
# {"book" : "Bạn ko thông minh lắm đâu",
# "description": "funny psy book",
# },
# {
# "animal": "Cat and Dog",
# "description":"for animal"
# },
# {
# "dictonary": "dict la ban",
# "description":"dictionary for everyone"
# }
# ]
# #5. Insert document into Collection
# # games.insert_one(new_game)
# for blog in list_blogs:
#     blogs.insert_one(blog)


all_game = games.find()

for game in all_game:
    print(game['name'])
