#d_b.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


d_b = Flask(__name__)
d_b.config.from_object(os.environ['APP_SETTINGS'])
d_b.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(d_b)

from models import Result


@d_b.route('/')
def hello():
	return "Hello World!"
	

@d_b.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)
	
	
if __name__ == '__main__':
	app.run()
	
	