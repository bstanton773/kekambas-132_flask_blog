from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)
# Set the app's secret key
app.config['SECRET_KEY'] = 'you-will-never-guess'


from . import routes
