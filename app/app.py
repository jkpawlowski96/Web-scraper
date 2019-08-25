from flask import Flask, Response
from bs4 import BeautifulSoup
import urllib.request as urllib2
import image_scraper
from data import *


app= Flask(__name__)


@app.route("/")
def home():
    return "hello world"

"""-----------------------------------------------
Command service to download resources form website
"""


@app.route('/t/<path:adress>')
def download_text(adress):
    page = urllib2.urlopen(adress)
    web_text = get_text(page)
    
    return string_to_file(web_text)
    #return web_text

@app.route('/i/<path:adress>')
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

def get_text(html):
    soup = BeautifulSoup(html, 'html.parser')
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
