# celery_config.py
from __future__ import absolute_import
from datetime import timedelta

broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'

imports = ('google_reviews_chatbot',)

beat_schedule = {
    'fetch-google-reviews-every-10-minutes': {
        'task': 'google_reviews_chatbot.fetch_and_respond_reviews',
        'schedule': timedelta(minutes=10),
    },
}
