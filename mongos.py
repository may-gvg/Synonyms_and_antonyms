import json
from bson.json_util import dumps
from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    con_str = "mongodb+srv://mongo:letgo666@cluster0.obxcw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(con_str)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['mongotest']


# This is added so that many files can reuse the function get_database()
def insert_sentences(sentences):
    # Get the database
    mydb = get_database()
    mycol = mydb["mongotest"]

    for sentence in sentences:
        x = mycol.insert_one(sentence)

    collection = mycol
    cursor = collection.find({})
    with open('collection.json', 'w') as file:
        json.dump(json.loads(dumps(cursor)), file)
