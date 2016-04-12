# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient("localhost", 12345)

db = client.users

c = db.users.find()
for i in c:
    print i

flag = db.users.remove({u"name": u"huiyang"})
print flag

