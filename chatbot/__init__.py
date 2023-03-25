# chatbot/__init__.py
from .routes import app
from .celery_tasks import fetch_and_respond_reviews
