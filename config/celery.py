import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTING_MODULE','your_project_name.settings')

app = Celery('kelasoor_SupportPanel')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()