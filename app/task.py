
from text import get_text, string_to_file
from images import get_images_bytes, get_images_links
from database import data_add_resource

def scrap_webiste(adress):	
	web_text = get_text(adress)
	web_images_l = get_images_links(adress)
	web_images_b = get_images_bytes(web_images_l)
	row = {}
	row['Adress']=adress
	row['Text']=web_text
	row['Images']=web_images_b
	row['Images_links']=web_images_l
	if data_add_resource(row) is True: #and images in the future 
		return True
	else:
		return False
    
    