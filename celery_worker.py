# celery_worker.py
from __future__ import absolute_import
from celery import Celery

app = Celery('google_reviews_chatbot')
app.config_from_object('celery_config')
