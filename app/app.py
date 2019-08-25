from flask import Flask, Response
from bs4 import BeautifulSoup
import urllib.request as request
import image_scraper
from data import *


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
	web_images = get_images(adress)
	if data_add(adress=adress,text=web_text,images=web_images) is True: #and images in the future 
		return 'succes'
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
	page = request.urlopen(adress)
	web_text = get_text(page)
	
	return string_to_file(web_text)
	#return web_text

@app.route('/file/i/<path:adress>')
def download_images(adress):
	data = image_scraper.scrape_images(adress)

	return string_to_file(str(data))
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

def get_text(adress):
	page = request.urlopen(adress)
	soup = BeautifulSoup(page, 'html.parser')
	#soup.find_all("div")
	web_text = ''
	for div in soup.find_all("div"):
		web_text += div.text+' '
	#page = bs4.BeautifulSoup(html, 'html')
	#web_text = page.get_text(separator='\n')
	web_text = web_text.replace('\\n','')
	web_text = web_text.replace('\n','')
	web_text = web_text.replace('  ','')

	return web_text


def get_images(adress):
	page = request.urlopen(adress)
	soup = BeautifulSoup(page, 'html.parser')
	tags=soup.findAll('img')
	print(tags)
	images = []
	for img in tags:
		try:
			images.append(img['src'])
		except:
			pass
		
	return images