import urllib.request as request
from bs4 import BeautifulSoup


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