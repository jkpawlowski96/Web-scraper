from text import get_text, string_to_file
from images import get_images_bytes, get_images_links
from database import data_add_resource, adress_done, adress_working
import threading
import time
from random import randint

"""Queue of adress to scrap and add resources to database"""


def init_scrapper():
	mythread = Scrapper(name = "Thread-{}".format(1))  # ...Instantiate a thread and pass a unique ID to it
	mythread.start()                                   # ...Start the thread, invoke the run method
	return mythread


def scrap_website(adress):	
	web_text = get_text(adress)
	web_images_l = get_images_links(adress)
	web_images_b = get_images_bytes(web_images_l)
	row = {}
	row['Address']=adress
	row['Text']=web_text
	row['Images']=web_images_b
	row['Images_links']=web_images_l
	if data_add_resource(row) is True: #and images in the future 
		return True
	else:
		return False

class Scrapper(threading.Thread):

	job_queue=[]

	def run(self):
		while(True):
			try:
				adress = self.job_queue.pop(0)  # Take adress to do from the stack
			except:
				time.sleep(2)
				continue
			try:
				adress_working(adress,value=True)
				results = scrap_website(adress)
				if results is True:
					adress_working(adress,value=False)  # Job is not working anymore. Adress is already in database
					continue
					# "Thread-x finished!"
				else:
					continue  # Something was wrong
			except:
				pass
	
	def process_order(self, adress):
		self.job_queue.append(adress)




