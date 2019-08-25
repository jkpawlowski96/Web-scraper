import pandas as pd
import numpy as np
from flask import make_response

'''
Data from scraped websites
'''
data = pd.DataFrame(columns=['Adress','Text','Images_links','Images_bytes'])


def data_add(row):
    global data
    if row['Adress'] in data.Adress.values:
        return False
    try:
        data = data.append(row, ignore_index=True)
    except:
        return False
    return True

def data_display():
    global data
    return data.to_html()
    
def data_images_display():
    global data
    
    return data[['Adress','Images_links']].to_html()

def data_text_display():
    global data
    return data[['Adress','Text']].to_html()

def data_csv():
    global data
    resp = make_response(data.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=data.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp