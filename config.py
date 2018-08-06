import os
import sys
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Load local .env file for credentials
dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY')