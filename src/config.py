import os

class Config:
    def get_namespace():
        return os.getenv('NAMESPACE')

    def get_service():
        return os.getenv('SERVICE')