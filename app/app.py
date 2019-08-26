from flask import Flask, Response

from database import data_export, adress_done, adress_working
from task import scrap_webiste
app= Flask(__name__)


@app.route("/")
def home():
	return "hello world"

"""-----------------------------------------------
Command service to download resources form website
"""
@app.route('/order/<path:adress>')
def order(adress):
	if adress_done(adress) is False and adress_working(adress) is False:
		if scrap_webiste(adress):
			return 'accepted'
		else:
			return 'error'
	else:
		return 'data in progress or exicts'
"""-----------------------------------------------
Export resources form databese
"""
@app.route('/export/')
def export():
	return data_export()


@app.route('/export/<path:adress>')
def export_path(adress): 
	return data_export(query={'Adress':adress})





