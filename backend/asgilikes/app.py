import falcon
import falcon.asgi

from .likes import AsyncLikesResource


def create_app(config=None):
    app = falcon.asgi.App()

    async_likes_resource = AsyncLikesResource()
    app.add_route('/api/likes', async_likes_resource)

    return app
