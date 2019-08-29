import urllib.request as request
from bs4 import BeautifulSoup
from flask import Response


def get_text(address):
	"""
	Scrap website from text
	:param address: website address example: https://www.youtube.com/
	:return: text
	"""
	page = request.urlopen(address)  # as html
	soup = BeautifulSoup(page, 'html.parser')

	#  scrap text from divs in a look
	web_text = ''
	for div in soup.find_all("div"):
		web_text += div.text+' '

	# fix mishmash
	web_text = web_text.replace('\\n', '')
	web_text = web_text.replace('\n', '')
	web_text = web_text.replace('  ', '')

	return web_text


def string_to_file(data):
	"""
	Convert string to text file
	:param data: text data
	:return:  text file
	"""
	return Response(
	data,
	mimetype="text/txt",
	headers={"Content-disposition":
			"attachment; filename=file.txt"})
