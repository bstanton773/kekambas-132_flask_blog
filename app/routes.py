from app import app
from flask import render_template

# Create our first route
@app.route('/')
def index():
    name = 'Brian'
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    return render_template('index.html', first_name=name, last_name='Stanton', colors=colors)

# Create a second route
@app.route('/new')
def new():
    name = 'Brian Stanton'
    return f"<h1>Hello {name}, this is a new route!</h1>"
