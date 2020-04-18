from pymongo import MongoClient


MONGO_URL = 'mongodb://127.0.0.1:27017'


class MongoDB(object):
    def __init__(self, kind='doctors_info', type='pinganApp'):
        # 建立数据库连接
        self.client = MongoClient(MONGO_URL)
        # 获取要操作的集合
        self.mongo = self.client[type][kind]

    def insert_one(self, dic):
        '''实现插入功能'''
        self.mongo.insert_one(dic)
        # print(f'插入内容：{dic}')

    def find(self):
        '''实现查找功能'''

        cursor = self.mongo.find()

        return cursor