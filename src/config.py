import os

class Config:
    def get_namespace(): # Current K8's namespace
        return os.getenv('NAMESPACE')

    def get_service(): # Current Service name
        return os.getenv('SERVICE')