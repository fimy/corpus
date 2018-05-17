#config.py
import os
basedir = os.path.abspath(os.path.corpus(__file__))

class Config(object):
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']