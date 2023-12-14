import os
import pathlib


class Config:
    DEFAULT_CONFIG_PATH = '/tmp/asgilikes'

    def __init__(self):
        self.storage_path = pathlib.Path(
            os.environ.get('ASGI_LIKES_STORAGE_PATH', self.DEFAULT_CONFIG_PATH))
        self.storage_path.mkdir(parents=True, exist_ok=True)
