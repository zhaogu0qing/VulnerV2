# coding:utf8
"""
Created by zhaoguoqing on 18/12/8
"""
import pymongo
import sys
sys.path.append('..')
from spider.cnnvd.cnnvd.settings import MONGO_URI

client = pymongo.MongoClient(MONGO_URI)
db = client['zgq']
collection = db['Vulner']
i = 0
for item in collection.find().batch_size(50):
    i += 1
    collection.update({'_id': item['_id']}, {'$set': {'source': 'cnnvd'}})
    print(i, item['_id'])
