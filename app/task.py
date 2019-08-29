from text import get_text, string_to_file
from images import get_images_bytes, get_images_links
from database import data_add_resource, address_done, address_working
import threading
import time
from random import randint


def init_scrapper():
	"""
	Initialize background thread to scrap websites
	:return: thread
	"""
	mythread = Scrapper(name = "Thread-{}".format(1))  # ...Instantiate a thread and pass a unique ID to it
	mythread.start()                                   # ...Start the thread, invoke the run method
	return mythread


def scrap_website(address):	
	"""
	Scrap text and images from website
	:param address: website address example: https://www.youtube.com/
	:return: true value if done
	"""
	web_text = get_text(address)  # scrap text
	web_images_l = get_images_links(address)  # scrap images
	web_images_b = get_images_bytes(web_images_l)  # images into bytes
	row = {}
	row['Address']=address
	row['Text']=web_text  
	row['Images']=web_images_b   
	row['Images_links']=web_images_l 
	#  add resource to database
	if data_add_resource(row) is True: #and images in the future 
		return True
	else:
		return False


class Scrapper(threading.Thread):
	"""
	Scrapping thread class
	"""
	# Queue of address to scrap and add resources to database
	job_queue=[]

	def run(self):
		while(True):
			try:
				address = self.job_queue.pop(0)  # Take adress to do from the stack
			except:
				time.sleep(2)
				continue
			# first check resources
			if address_done(address) is True: 
				continue
			# and working tasks..
			if address_working(address) is True: 
				continue	
			# starting process
			try:
				address_working(address,value=True)  # add as working task
				results = scrap_website(address)  # scrap website
				if results is True:
					address_working(address,value=False)  # Job is not working anymore. Adress is already in database
					continue
	
				else:
					continue  # Something was wrong
			except:
				pass
	
	def process_order(self, address):
		"""
		Take and order to scrap website
		:param address: website address example: https://www.youtube.com/
		:return:
		"""
		self.job_queue.append(address)




