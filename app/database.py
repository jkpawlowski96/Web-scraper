from pymongo import MongoClient
import pandas as pd
from bson.json_util import dumps
#from flask.json import dumps
#from json import dumps
from flask import make_response


def db_init():
    client = MongoClient("mongodb+srv://admin:semantive@semantive-ltgni.mongodb.net/test?retryWrites=true&w=majority")
    #client['scrap'].dropDatabase()
    db = client['scrap'] 
    db['resources'].drop()
    db['tasks'].drop()
    return db

db = db_init()


def data_add_task(adress):
    global db
    db.tasks.insert_one({'Adress':adress})
    return True

def data_add_resource(row):
    global db
    db.resources.insert_one(row)
    return True

def adress_working(adress,  value=None):
    global db
    if value is True:
        db.tasks.insert_one({'Adress':adress})
        return True

    if value is False:
        db.tasks.delete_many({'Adress':adress})
        return False

    x = list(db.tasks.find({'Adress':adress}))
    if len(x)==0:
        return False
    else:
        return True

def data_export(colums={'Adress':1,'Text':1,'Images':1,'Images_links':1,'_id':0},query={}, download=False):
    global db

    data = db.resources.find(query,colums)
    data = list(data)
    data = dumps(data)
    if download is False:
        return data
    else: 
        resp = make_response(data)
        resp.headers["Content-Disposition"] = "attachment; filename=data.json"
        resp.headers["Content-Type"] = "text/json"
        return resp
        
     


def adress_done(adress):
    global db
    x = list(db.resources.find({'Adress':adress}))
    if len(x)==0:
        return False
    else:
        return True
  


def db_to_df(query={}, no_id=True):
    """ Read from Mongo and Store into DataFrame """
    global db
  
    # Make a query to the specific DB and Collection
    cursor = db.resources.find(query)
    
    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id and '_id' in df:
        del df['_id']

    return df
  
def json_to_scv(data, download=False):
    data = pd.read_json(data)

    if download is False:
        return data.to_html()

    data = data.to_csv(index=False)
    resp = make_response(data)
    resp.headers["Content-Disposition"] = "attachment; filename=data.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp