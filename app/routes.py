from app import app

# Create our first route
@app.route('/')
def index():
    name = 'Brian'
    return '<h2>Hello World!!</h2>'

# Create a second route
@app.route('/new')
def new():
    name = 'Brian Stanton'
    return f"<h1>Hello {name}, this is a new route!</h1>"
