from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create an instance of the Flask class
app = Flask(__name__)
# Configure our app with the Attributes and Values from the Config class
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app)
# Create an instance of Migrate to track our database migrations
migrate = Migrate(app, db)
# Create an instance of LoginManager to handle authentication
login = LoginManager(app)


from . import routes, models
