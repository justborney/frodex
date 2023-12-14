import falcon
import falcon.asgi

from .config import Config
from .likes import AsyncLikesResource


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource:
    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            '\nTwo things awe me most, the starry sky '
            'above me and the moral law within me.\n'
            '\n'
            '    ~ Immanuel Kant\n\n'
        )


def create_app(config=None):
    config = config or Config()
    # falcon.asgi.App instances are callable ASGI apps...
    # in larger applications the app is created in a separate file
    app = falcon.asgi.App()

    # Resources are represented by long-lived class instances
    things = ThingsResource()
    async_likes_resource = AsyncLikesResource()

    # things will handle all requests to the '/things' URL path
    app.add_route('/things', things)
    app.add_route('/alikes', async_likes_resource)

    return app
