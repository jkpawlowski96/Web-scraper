from PIL import Image
import urllib.request as request
from io import BytesIO, StringIO
import numpy as np


def image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


def image_to_bytes(image:Image):
    imgByteArr = BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

def bytes_to_image(bytes):
    return Image.open(BytesIO(img))
