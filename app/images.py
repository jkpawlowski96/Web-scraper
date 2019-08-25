from PIL import Image
import urllib.request as request
import requests
from io import BytesIO, StringIO
from bs4 import BeautifulSoup
import numpy as np

def get_images_links(adress):
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

def get_images_bytes(links):
	images=[]
	for link in links:
		try:
			img = image_from_url(link)
			img = image_to_bytes(img)
			images.append(img)
		except:
			pass
	return images


def image_from_url(url):
	request
	response = requests.get(url)
	return Image.open(BytesIO(response.content))


def image_to_bytes(image:Image):
	imgByteArr = BytesIO()
	image.save(imgByteArr, format=image.format)
	imgByteArr = imgByteArr.getvalue()
	return imgByteArr

def bytes_to_image(bytes):
	return Image.open(BytesIO(bytes))
