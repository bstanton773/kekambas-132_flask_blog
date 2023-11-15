from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

# Create an instance of the Flask class
app = Flask(__name__)
# Configure our app with the Attributes and Values from the Config class
app.config.from_object(Config)

# Add CORS to our app
CORS(app)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)
# Create an instance of Migrate to track our database migrations
migrate = Migrate(app, db)
# Create an instance of LoginManager to handle authentication
login = LoginManager(app)
login.login_view = 'login'
# login.login_message = 'You have to be logged in to do that you fool!'

# register the api blueprint with our app
from app.blueprints.api import api
app.register_blueprint(api)

from . import routes, models
