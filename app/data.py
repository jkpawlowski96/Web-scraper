import pandas as pd
import numpy as np

data = pd.DataFrame(columns=['Adress','Text','Images'])

def data_add(adress=np.nan, text=np.nan, images=np.nan):
    global data
    try:
        data = data.append({'Adress': adress,'Text':text, 'Images':images}, ignore_index=True)
        return True
    except:
        return False
def data_display():
    global data
    return data.to_html()
    
def data_images_display():
    global data
    
    return data[['Adress','Images']].to_html()

def data_text_display():
    global data
    return data[['Adress','Text']].to_html()