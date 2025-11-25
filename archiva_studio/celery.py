import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archiva_studio.settings')
app = Celery('archiva_studio')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()