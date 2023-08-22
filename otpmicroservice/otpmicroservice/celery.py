from __future__ import absolute_import
import os,django
from celery import Celery



import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "otpmicroservice.settings")
django.setup()

# django.setup()



app = Celery ('otpmicroservice')

app.config_from_object('django.conf:settings' , namespace='CELERY')

app.autodiscover_tasks()
