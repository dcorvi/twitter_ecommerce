import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'temp'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # set the uri for the database location, this db will be locally stored through sqlite database
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'app.db')

    # use this when setting up postgress
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:password@localhost:5432/twitter'


# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or '<db_type>' or 'postgresql://<username>:<password>@<host_address>:<port>/<database_name>'


# get API key
# class Config(object):
#     WEATHER_API_KEY = '433ee877d8f648a1875a418c7251cb35'
