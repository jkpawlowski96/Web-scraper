import urllib.request as request
from bs4 import BeautifulSoup
from flask import Response

def get_text(adress):
	page = request.urlopen(adress)
	soup = BeautifulSoup(page, 'html.parser')

	web_text = ''
	for div in soup.find_all("div"):
		web_text += div.text+' '
	#page = bs4.BeautifulSoup(html, 'html')
	#web_text = page.get_text(separator='\n')
	web_text = web_text.replace('\\n','')
	web_text = web_text.replace('\n','')
	web_text = web_text.replace('  ','')

	return web_text


def string_to_file(data):
	return Response(
	data,
	mimetype="text/txt",
	headers={"Content-disposition":
			"attachment; filename=file.txt"})
