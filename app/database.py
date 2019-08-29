from pymongo import MongoClient
import pandas as pd
from bson.json_util import dumps
from flask import make_response


def db_init():
    """
    Initialize database connection and clear data in collection
    :return: MongoDB reference object
    """
    client = MongoClient("mongodb+srv://admin:semantive@semantive-ltgni.mongodb.net/test?retryWrites=true&w=majority")
    # client['scrap'].dropDatabase()
    db = client['scrap']
    db['resources'].drop()
    db['tasks'].drop()
    return db

# init database
db = db_init()


def data_add_task(address):
    """
    Add new working task o database
    :param address: website address example: https://www.youtube.com/
    :return: True value as job done
    """
    global db
    db.tasks.insert_one({'Address': address})
    return True


def data_add_resource(row):
    """
    Add new working task o database
    :param row: Row to add
    :return: True value as job done
    """
    global db
    db.resources.insert_one(row)
    return True


def address_working(address, value=None):
    """
    Find, insert or delete from database task address
    :param address: website address example: https://www.youtube.com/
    :param value: True: add , False: remove, default: find
    :return:
    """
    global db
    if value is True:
        db.tasks.insert_one({'Address': address})
        return True

    if value is False:
        db.tasks.delete_many({'Address': address})
        return False

    x = list(db.tasks.find({'Address': address}))
    if len(x) == 0:
        return False
    else:
        return True


def data_export(colums={'Address': 1, 'Text': 1, 'Images': 1, 'Images_links': 1, '_id': 0}, query={}, download=False):
    """
    Export found data from database
    :param colums: Columns to export
    :param query: Filter of data
    :param download: True: return file, default: return view
    :return: data
    """
    global db
    data = db.resources.find(query, colums)
    data = list(data)
    data = dumps(data)
    if download is False:
        return data
    else:
        resp = make_response(data)
        resp.headers["Content-Disposition"] = "attachment; filename=data.json"
        resp.headers["Content-Type"] = "text/json"
        return resp


def address_done(address):
    """
    Check if address is already in done resources
    :param address: website address example: https://www.youtube.com/
    :return: result
    """
    global db
    x = list(db.resources.find({'Address': address}))
    if len(x) == 0:
        # not found
        return False
    else:
        # found
        return True


def db_to_df(query={}, no_id=True):
    """
    Read from Mongo and transform into DataFrame
    :param query: data filter
    :param no_id: don't include id field
    :return: DataFrame object
    """
    global db

    # Make a query to the specific DB and Collection
    cursor = db.resources.find(query)

    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id and '_id' in df:
        del df['_id']

    return df


def json_to_scv(data, download=False):
    """
    Transform json to csv
    :param data: json with data
    :param download: True: return file, default: return view
    :return: csv
    """
    data = pd.read_json(data)

    if download is False:
        # as a html view
        return data.to_html()
    # to file
    data = data.to_csv(index=False)
    resp = make_response(data)
    resp.headers["Content-Disposition"] = "attachment; filename=data.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
