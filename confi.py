
from pymongo import MongoClient
def client():
    URL= 'mongodb+srv://swaty:swaty@cluster0.ueh59.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE'
    client = MongoClient(URL)
    return client

CLIENT= client()