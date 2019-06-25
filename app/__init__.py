# setup imports
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# setup app variables
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

# you have to instantiate the database variables after the config has been set
# reason is tat the cofig holds tje ;ppcatopm of the dayabase
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# app variables for login
login = LoginManager(app)

# when a page requies somebody to be looged in, the application will by default sent them back to the previous pahe, however we will make them go back to the login instead
login.logan_view = 'login'

# go to routes
from app import routes
