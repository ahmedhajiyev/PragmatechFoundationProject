from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
from flask_migrate import Migrate
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = '5f47fc632a585184688be1969d20bfcb'

#PHOTO UPLOAD
import os
from werkzeug.utils import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')
app.config['UPLOAD__FOLDER'] = UPLOAD_FOLDER


from PortfolioProject.controlers import *