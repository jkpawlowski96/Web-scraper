from flask import Flask, Response
from bs4 import BeautifulSoup
import urllib.request as urllib2
#from selectolax.parser import HTMLParser

app= Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route('/o/<path:adress>')
def show_subpath(adress):
    page = urllib2.urlopen(adress)
    web_text = get_text(page)
    
    #return string_to_file(web_text)
    return web_text

    
def string_to_file(data):
    return Response(
        data,
        mimetype="text/txt",
        headers={"Content-disposition":
                 "attachment; filename=file.txt"})


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
