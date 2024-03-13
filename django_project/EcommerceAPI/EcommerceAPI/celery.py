#  Celery settings
from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','EcommerceAPI.settings')

app = Celery('EcommerceAPI')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kathmandu')
app.config_from_object(settings,namespace='CELERY')


#  Celery Beat settings
# app.conf.beat_schedule = {
#      '  send-mail':{
#          'task': 'email_app.tasks.send_mail_func',
#          'schedule': crontab(hour=17,minute=23),
#      }   
# }

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')