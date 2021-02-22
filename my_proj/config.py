import os

BASE_DIR = os.path.dirname(__file__)

SQLAlCHEMY_TRACK_MODIFICATIONS = False

SQLAlCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))

SECRET_KEY = develpment