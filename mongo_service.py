# from pymongo import MongoClient, ASCENDING, DESCENDING
# from datetime import datetime

# connection_string = "mongodb://localhost:27017"

# def save_chat(data: dict):
#     data["timestamp"] = datetime.now()
#     with MongoClient(connection_string) as client:
#         client["UET"]["chat"].insert_one(data)


# def fetch_chat(user_id: str):
#         with MongoClient(connection_string) as client:
#             return list(client["UET"]["chat"].find({"user_id" : user_id})).sort('timestamp', ASCENDING)


from pymongo import MongoClient, ASCENDING, DESCENDING
from datetime import datetime

connection_string = "mongodb://localhost:27017/"

def save_chat(data:dict):
    data['timestamp'] = datetime.now()
    with MongoClient(connection_string) as client:
        client['uet_demo']['chat'].insert_one(data)

def fetch_chat(userid:str):
    with MongoClient(connection_string) as client:
        return list(client['uet_demo']['chat'].find({'user_id':userid}).sort('timestamp', ASCENDING))
    

# save_chat({"role" : "user", "content" : "hello"})
