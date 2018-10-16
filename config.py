import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_key = os.environ.get('SECRET_KEY') or 'generative-design-data'
    WTF_CSRF_SECRET_KEY= "a csrf secret key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
