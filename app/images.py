from PIL import Image
import urllib.request as request
import requests
from io import BytesIO, StringIO
from bs4 import BeautifulSoup
import numpy as np


def get_images_links(address):
    """
    Scrap website from images links
    :param address: website address example: https://www.youtube.com/
    :return: images links
    """
    page = request.urlopen(address)  # html
    soup = BeautifulSoup(page, 'html.parser')
    tags = soup.findAll('img')  # all images
    print(tags)
    images = []
    # scrap from images links in a look
    for img in tags:
        try:
            images.append(img['src'])
        except:
            pass
    return images


def get_images_bytes(links):
    """
    Transform images links into bytes format to load as Pillow object later
    :param address: list of images links
    :return: images as bytes
    """
    images = []
    # transform to bytes in a look
    for link in links:
        try:
            img = image_from_url(link)  # download as Pillow object
            img = image_to_bytes(img)  # transform into bytes format as a universal solution
            images.append(img)  # add
        except:
            pass
    return images


def image_from_url(url):
    """
    Download image from url
    :param url: url of image
    :return: image Pillow object
    """
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


def image_to_bytes(image: Image):
    """
    Transform image to bytes format
    :param image: image Pillow object
    :return: bytes
    """
    imgByteArr = BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def bytes_to_image(bytes):
    """
    Inverse transform of bytes into image
    (To use for others)
    :param bytes: mage in bytes format
    :return: image Pillow object
    """
    return Image.open(BytesIO(bytes))
