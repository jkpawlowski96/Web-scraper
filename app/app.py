from flask import Flask, Response

from text import get_text
from images import get_images_bytes, get_images_links
from data import data_add, data_display, data_text_display, data_images_display, data_images_display

app= Flask(__name__)


@app.route("/")
def home():
	return "hello world"

"""-----------------------------------------------
Command service to download resources form website
"""
@app.route('/order/<path:adress>')
def order(adress):
	web_text = get_text(adress)
	web_images_l = get_images_links(adress)
	web_images_b = get_images_bytes(web_images_l)
	row = {}
	row['Adress']=adress
	row['Text']=web_text
	row['Images_links']=web_images_l
	row['Images_bytes']=web_images_b
	if data_add(row) is True: #and images in the future 
		return 'succed :)'
	else:
		return 'FAILED!!!'
	
	#return web_text

"""-----------------------------------------------
Command service to download resources form website
"""
@app.route('/resources/display/')
def display(): 
	return data_display()

@app.route('/resources/display/images')
def display_images(): 
	return data_images_display()

@app.route('/resources/display/text')
def display_text(): 
	return data_text_display()

"""-----------------------------------------------
Download resources form website
"""
@app.route('/file/t/<path:adress>')
def download_text(adress):
	web_text=get_text(adress)
	
	return string_to_file(web_text)
	#return web_text


"""------------------------------------------------
Downlaod all resources as csv file
"""





def string_to_file(data):
	return Response(
	data,
	mimetype="text/txt",
	headers={"Content-disposition":
			"attachment; filename=file.txt"})

def images_to_file(data):
	return Response(data,
		mimetype='application/zip',
		headers={'Content-Disposition':'attachment;filename=images.zip'})




