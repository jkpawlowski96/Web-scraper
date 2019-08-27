from flask import Flask, Response
from database import data_export, adress_done, adress_working
from task import scrap_webiste, make_celery

app= Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

@app.route("/")
def home():
	return "hello world"

"""-----------------------------------------------
Command service to download resources form website
"""
@app.route('/order/<path:adress>')
def order(adress):
	if adress_done(adress) is False and adress_working(adress) is False:
		task = process_order.delay(adress)
		return str(task)
	else:
		return 'data in progress or exicts'

@celery.task()
def process_order(adress):
	scrap_webiste(adress)

"""-----------------------------------------------
Export resources form databese
"""
@app.route('/export/')
def export():
	return data_export()


@app.route('/export/<path:adress>')
def export_path(adress): 
	return data_export(query={'Adress':adress})





