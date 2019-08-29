from flask import Flask, Response, send_from_directory
from database import data_export, adress_done, adress_working, json_to_scv
from task import init_scrapper

# flask app
app = Flask(__name__)
# website scraper
scrapper = init_scrapper()


@app.route("/")
def home():
	"""
	Homepage
	:return:
	"""
	return  '<h1>Hello Semantive!</h1>'


"""-----------------------------------------------------------------
Command services to download resources form website,
or check status of task
-----------------------------------------------------------------"""


@app.route('/order/<path:address>')
def order(address):
	"""
	Function add task to scrap website resources
	:param address: website address example: https://www.youtube.com/
	:return: service_answer
	"""
	if adress_done(address) is False:
		# resources are not in database
		if adress_working(address) is False:
			# service is not scraping given address
			scrapper.process_order(address)  # scrap website
			return 'starting'
		else:
			# # service is scraping given address
			return 'in progress'
	else:
		# resources are already in database
		return 'finished'


"""-----------------------------------------------------------------
Export resources form database
-----------------------------------------------------------------"""


@app.route('/export/json/')
def export_json():
	"""
	Display all data in json
	:return: json
	"""
	return data_export()


@app.route('/export/csv/')
def export_scv():
	"""
	Display all data in csv
	:return: csv
	"""
	return json_to_scv(data_export())


@app.route('/export/json/<path:address>')
def export_json_path(address):
	"""
	Display selected data in json
	:param address: website address example: https://www.youtube.com/
	:return: json
	"""
	return data_export(query={'Address': address})


@app.route('/export/csv/<path:address>')
def export_csv_path(address):
	"""
	Display selected data in csv
	:param address: website address example: https://www.youtube.com/
	:return: csv
	"""
	return json_to_scv(data_export(query={'Address': address}))


"""-----------------------------------------------------------------
Download resources form databese
-----------------------------------------------------------------"""


@app.route('/download/json/')
def download_json():
	"""
	Download all data in json file
	:return: json file
	"""
	return data_export(download=True)

@app.route('/download/csv/')
def download_scv():
	"""
	Download all data in csv file
	:return: csv file
	"""
	return json_to_scv(data_export(), download=True)


@app.route('/download/json/<path:address>')
def download_json_path(address):
	"""
	Download selected data in json file
	:param address: website address example: https://www.youtube.com/
	:return: json file
	"""
	return data_export(query={'Address': address}, download=True)


@app.route('/download/csv/<path:address>')
def download_csv_path(address):
	"""
	Download selected data in csv file
	:param address: website address example: https://www.youtube.com/
	:return: json file
	"""
	return json_to_scv(data_export(query={'Address': address}), download=True)


if __name__ == "__main__":
	app.run(host="0.0.0.0")