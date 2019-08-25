import pandas as pd
import numpy as np

data_global = pd.DataFrame(columns=['Adress','Text','Images'])

def data_add(adress=np.nan, test=np.nan, images=np.nan, df=data_global):
    try:
        df = df.append({'Adress': adress,'Text':text, 'Images':images}, ignore_index=True)
        return True
    except:
        return False
