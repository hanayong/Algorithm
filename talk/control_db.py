from pymongo import MongoClient

class control():
    def __init__(self, db_name, col_name):
        client = MongoClient('localhost:27017')
        self.db = client[db_name]
        self.col = self.db[col_name]
        self.num = 0


    def input_doc(self, word):
        2
        self.col.insert(dict)

