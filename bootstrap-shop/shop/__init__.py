import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from flask_wtf import CSRFProtect
# from flask_migrate import Migrate

#basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

from shop import routes