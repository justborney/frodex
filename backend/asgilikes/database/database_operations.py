import psycopg2
from psycopg2 import sql
from falcon import HTTPInternalServerError
from celery import Celery

app = Celery(__name__)
app.conf.broker_url = 'redis://redis:6379/0'


def increment_likes_in_database_async(like_data):
    app.send_task('tasks.increment_likes', args=[like_data])

