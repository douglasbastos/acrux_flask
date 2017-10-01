import os

RUN_DEBUG = True
RUN_USE_RELOADER = True
RUN_HOST = 'localhost'
RUN_PORT = 5000

MONGODB_DB = "noticias"
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_files')
