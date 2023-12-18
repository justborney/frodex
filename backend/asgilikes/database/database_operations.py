import asyncpg

from falcon import HTTPInternalServerError
from celery import Celery

from ..config_data.read_env import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    PG_HOST,
    PG_PORT,
    CELERY_BROKER,
)

app = Celery(__name__)
app.conf.broker_url = CELERY_BROKER


async def connect_to_postgres():
    return await asyncpg.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
        host='localhost',
        port='5432',
    )


def increment_likes_in_database_async(like_data):
    app.send_task('tasks.increment_likes', args=[like_data])


@app.task
async def get_likes_async():
    conn = await connect_to_postgres()

    try:
        query = "SELECT COUNT(*) FROM likes;"
        result = await conn.fetchval(query)

        return result

    except Exception as e:
        raise HTTPInternalServerError(description=str(e))

    finally:
        await conn.close()


