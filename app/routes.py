from app import app
from flask import render_template
# Import the SingUpForm class from forms
from app.forms import SignUpForm

# Create our first route
@app.route('/')
def index():
    return render_template('index.html')

# Create a second route
@app.route('/signup')
def signup():
    # Create an instance of the SignUpForm
    form = SignUpForm()
    return render_template('signup.html', form=form)
