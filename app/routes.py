from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
# Import the SignUpForm, LoginForm, and PostForm classes from forms
from app.forms import SignUpForm, LoginForm, PostForm
# Import the User model from models
from app.models import User, Post

# Create our first route
@app.route('/')
def index():
    posts = db.session.execute(db.select(Post)).scalars().all()
    return render_template('index.html', posts=posts)

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
        # print(first_name, last_name, username, email, password)

        # Check to see if we already have a User with that username or email
        check_user = db.session.execute(db.select(User).where( (User.username==username) | (User.email==email) )).scalars().all()
        if check_user:
            flash('A user with that username and/or email already exists')
            return redirect(url_for('signup'))
        # Create a new instance of the User class with the data from the form
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        # Add the new user object to the database
        db.session.add(new_user)
        db.session.commit()

        # log the newly created user in
        login_user(new_user)

        flash(f"{new_user.username} has been created!")

        # Redirect back to the home page
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=["GET","POST"])
def login():
    # Create an instance of the LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        # Get the data from the form
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        # Query the User table for a user with that username
        user = db.session.execute(db.select(User).where(User.username==username)).scalar()
        # Check if there is a user AND the password is correct for that user
        if user is not None and user.check_password(password):
            login_user(user, remember=remember_me)
            # log the user in via Flask-Login
            flash(f'{user.username} has succesfully logged in.')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username and/or password')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out')
    return redirect(url_for('index'))

@app.route('/create-post', methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        
        # Create an instance of Post with form data and logged in user's ID
        new_post = Post(title=title, body=body, user_id=current_user.id)
        # Add to the database
        db.session.add(new_post)
        db.session.commit()

        # flash a success message
        flash(f"{new_post.title} has been created")
        return redirect(url_for('index'))
    
    return render_template('create_post.html', form=form)
