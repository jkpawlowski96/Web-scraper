
from text import get_text, string_to_file
from images import get_images_bytes, get_images_links
from database import data_add_resource

from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


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
    
    