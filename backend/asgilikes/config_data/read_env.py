import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'frodex_likes')
PG_HOST = os.getenv('PG_HOST', 'pgdb')
PG_PORT = os.getenv('PG_PORT', '5432')
CELERY_BROKER = os.getenv('CELERY_BROKER', 'redis://redis:6379/0')
CELERY_BACKEND = os.getenv('CELERY_BACKEND', 'redis://redis:6379/0')
