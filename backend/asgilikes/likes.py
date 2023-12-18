import falcon

from .database.tasks import get_likes_async, increment_likes_async


class AsyncLikesResource:
    async def on_get(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET, POST')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        resp.text = await get_likes_async()

    async def on_post(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET, POST')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        request = await req.media
        await increment_likes_async(request)
        resp.status = falcon.HTTP_200

    async def on_options(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET, POST')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        resp.status = falcon.HTTP_200
