from pymongo import MongoClient

class Mongo:
    def __init__(self,database,collection,host='localhost',port=27017):
        self.client = MongoClient(host,port)
        self.database = self.client.get_database(database)
        self.collection = self.database.get_collection(collection)

    # 增
    def  insert(self,document):
        if isinstance(document,dict):
            r = self.collection.insert_one(document)
            return r.inserted_id
        else:
            r = self.collection.insert_many(document)
            return r.inserted_ids

    # 删
    def delete(self,filter):
        r = self.collection.delete_many(filter)
        return r.deleted_count
    # 改
    def modify(self,filter,document):
        r = self.collection.update_many(filter,{'$set':document})
        return r.modified_count
    # 查
    def find(self,filter):
        r = self.collection.find(filter)
        for i in r:
            print(i)

if __name__ == '__main__':
    document =[{'name':'大王'},{'name':'小王'}]
    client = Mongo('tf','student')
    r = client.find({'age':{'$gte':20}})

