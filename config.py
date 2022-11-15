import os
from models import *


SECRET_KEY = os.urandom(32)




class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/oca'
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode.
    DEBUG = True