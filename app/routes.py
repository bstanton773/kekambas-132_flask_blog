from app import app
from flask import render_template

# Create our first route
@app.route('/')
def index():
    return render_template('index.html')

# Create a second route
@app.route('/signup')
def signup():
    return render_template('signup.html')
