import os
from models import *
from  dotenv import load_dotenv


SECRET_KEY = os.urandom(32)
load_dotenv()
DB_URL=os.getenv("DB_URL")



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    SQLALCHEMY_DATABASE_URI = DB_URL
    print(SQLALCHEMY_DATABASE_URI)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode.
    DEBUG = True
    
    