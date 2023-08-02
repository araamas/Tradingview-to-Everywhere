import pymongo
from pymongo.mongo_client import MongoClient

PWD = '5gsCKHt4Dg4aSa8E'

class Database:
    def __init__(self):
        self.cluster_pwd = PWD
        # for a connection to local database (the connection string was from the mongo shell when i typed "mongosh"):
        # self.client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.3")

        # for a connection to remote database:
        self.client = MongoClient(f"mongodb+srv://samaara:{self.cluster_pwd}@cluster1.565lfln.mongodb.net/?retryWrites=true&w=majority")
        
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        self.db = self.client["test"]
        self.collection = self.db["Entries & Exits"]

    def add_doc(self, _type, direction, symbol, tframe, entry, tp, sl, chart_link, content, date):
        doc = {
            "type": _type,
            "direction": direction,
            "symbol": symbol,
            "tframe": tframe,
            "entry": entry,
            "tp": tp,
            "sl": sl,
            "chart_link": chart_link,
            "content": content,
            "date": date
        }
        return self.collection.insert_one(doc)

    def get_latest_doc(self):
        docs = self.collection.find_one(sort=[("_id", pymongo.DESCENDING)])
        return docs
    
    def delete_all(self):
        self.collection.delete_many({}) 

db = Database()
db.delete_all()
