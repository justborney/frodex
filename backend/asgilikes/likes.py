import falcon
import asyncio


class AsyncLikesResource:
    async def on_get(self, req, resp):
        resp.media = {'likes': await get_likes_from_database_async()}

    async def on_post(self, req, resp):
        await increment_likes_in_database_async()
        resp.status = falcon.HTTP_200
