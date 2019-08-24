from flask import Flask, Response
import bs4
import urllib.request
#from selectolax.parser import HTMLParser

app= Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route('/o/<path:adress>')
def show_subpath(adress):
    print('WEB adress: '+adress)
    web_text=adress
    webpage=str(urllib.request.urlopen(adress).read())
    web_text = get_text(webpage)
    
    return string_to_file(web_text)
    #return web_text

    
def string_to_file(data):
    return Response(
        data,
        mimetype="text/txt",
        headers={"Content-disposition":
                 "attachment; filename=file.txt"})


def get_text(html):
    page = bs4.BeautifulSoup(html, 'html')
    web_text = page.get_text(separator='\n')
    web_text = web_text.replace('\\n','')
    web_text = web_text.replace('\n','')
    web_text = web_text.replace('  ','')

    return web_text
