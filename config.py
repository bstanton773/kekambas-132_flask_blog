import os

basedir = os.path.abspath(os.path.dirname(__file__))
# 'C:\\Users\\bstan\\Documents\\codingtemple-kekambas-132\\week6\\flask_blog'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
