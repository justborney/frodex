import json

import asyncpg
from celery import Celery
from falcon import HTTPInternalServerError

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
        host=PG_HOST,
        port=PG_PORT,
    )


async def get_likes_async():
    conn = await connect_to_postgres()

    try:
        query = "SELECT post, likes FROM likes;"
        result = await conn.fetch(query)

        likes_data = json.dumps([{"post": str(row['post']), "likes": row['likes']} for row in result])

        return likes_data

    except Exception as e:
        raise HTTPInternalServerError(description=str(e))

    finally:
        await conn.close()


@app.task
async def increment_likes_async(like_data):
    conn = await connect_to_postgres()

    try:
        query = "UPDATE likes SET likes = likes + 1 WHERE post = $1;"
        await conn.execute(query, like_data['post'])

    except Exception as e:
        raise HTTPInternalServerError(description=str(e))

    finally:
        await conn.close()
