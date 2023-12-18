from falcon.errors import HTTPInternalServerError
from celery import Celery


app = Celery(__name__)
app.conf.broker_url = 'redis://redis:6379/0'


@app.task
def increment_likes(like_data):
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="myuser",
        password="mypassword",
        host="postgres"
    )

    cursor = conn.cursor()

    try:
        query = sql.SQL("INSERT INTO likes (user_id, timestamp) VALUES (%s, NOW());")
        cursor.execute(query, (like_data['user_id'],))

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise HTTPInternalServerError(description=str(e))

    finally:
        cursor.close()
        conn.close()
