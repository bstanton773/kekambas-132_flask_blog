from app import app
from flask import render_template, redirect, url_for
# Import the SingUpForm class from forms
from app.forms import SignUpForm

# Create our first route
@app.route('/')
def index():
    return render_template('index.html')

# Create a second route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Create an instance of the SignUpForm
    form = SignUpForm()
    if form.validate_on_submit():
        # Get the data from each of the fields
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, username, email, password)

        # Redirect back to the home page
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)
