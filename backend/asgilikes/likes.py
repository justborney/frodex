import falcon
import asyncio

from .database.database_operations import get_likes_async, increment_likes_async


class AsyncLikesResource:
    async def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET, POST')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        resp.body = await get_likes_async()

    async def on_post(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET, POST')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        await increment_likes_async()
        resp.status = falcon.HTTP_200
