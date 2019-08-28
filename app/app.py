from flask import Flask, Response
from database import data_export, adress_done, adress_working, json_to_scv
from task import init_Scrapper

app= Flask(__name__)

scrapper = init_Scrapper()

@app.route("/")
def home():
	return '<h1>hello world</h1>'

"""-----------------------------------------------
Command service to download resources form website,
or check status of task

"""
@app.route('/order/<path:adress>')
def order(adress):
	if adress_done(adress) is False:
		if adress_working(adress) is False:
			scrapper.process_order(adress)
			return 'starting'
		else:
			return 'in progress'
	else:
		return 'finished'

"""-----------------------------------------------
Export resources form databese
"""
@app.route('/export/json/')
def export_json():
	return data_export()

@app.route('/export/csv/')
def export_scv():
	return json_to_scv(data_export())

@app.route('/export/json/<path:adress>')
def export_json_path(adress): 
	return data_export(query={'Adress':adress})

@app.route('/export/csv/<path:adress>')
def export_csv_path(adress): 
	return json_to_scv(data_export(query={'Adress':adress})) 

"""-----------------------------------------------
Export resources form databese
"""

@app.route('/download/json/')
def download_json():
	return data_export(download=True)

@app.route('/download/csv/')
def download_scv():
	return json_to_scv(data_export(), download=True)

@app.route('/download/json/<path:adress>')
def download_json_path(adress): 
	return data_export(query={'Adress':adress},download=True)


@app.route('/download/csv/<path:adress>')
def download_csv_path(adress): 
	return json_to_scv(data_export(query={'Adress':adress}), download=True) 

if __name__=="__main__":
	app.run(host="0.0.0.0")