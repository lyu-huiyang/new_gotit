from pymongo import MongoClient

mc = MongoClient("localhost", 27017)

db = mc.users

c = db.users.find()

for i in c:
    print(i)