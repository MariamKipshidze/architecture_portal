import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'architecture_portal.settings')

app = Celery('architecture_portal')
app.config_from_object('django.conf')

# Load configuration from Django settings using the CELERY_ namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all installed Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
