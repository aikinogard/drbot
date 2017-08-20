import time
import datetime
import logging
from celery import Celery
from celery.schedules import crontab
from tasklib.send_email import load_email_configure, send_email
from tasklib.get_weather import get_weather

app = Celery('tasks', broker='redis://localhost:6379/0')

#periodic tasks
app.conf.beat_schedule = {
    'daily': {
        'task': 'tasks.daily_updates',
        'schedule': crontab(minute=0, hour=8)
    }
}

@app.task
def daily_updates():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    subject = 'Daily Updates from DrBOT %s' % now
    context = []
    context.append(get_weather('mountain view'))
    context.append(get_weather('irvine'))
    context.append(get_weather('shanghai'))
    context.append(get_weather('xian'))
    context = '\n'.join(context)
    send_email(subject, context, **load_email_configure())
