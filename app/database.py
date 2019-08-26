from pymongo import MongoClient
import pandas as pd
from bson.json_util import dumps

def db_init():
    client = MongoClient("mongodb+srv://admin:semantive@semantive-ltgni.mongodb.net/test?retryWrites=true&w=majority")
    #client['scrap'].dropDatabase()
    db = client['scrap'] 
    db['resources'].drop()
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

def adress_working(adress):
    global db
    x = list(db.tasks.find({'Adress':adress}))
    if len(x)==0:
        return False
    else:
        return True

def data_export(colums={'Adress':1,'Text':1,'Images':1,'Images_links':1,'_id':0},query={}):
    global db

    data = db.resources.find(query,colums)
    data = list(data)
    data = dumps(data)
    return data
     


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
  


df = db_to_df()
df.head()