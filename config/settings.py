import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

DATABASE_URL = os.environ.get('DATABASE_URL')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
