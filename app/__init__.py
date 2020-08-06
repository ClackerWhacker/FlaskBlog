from flask import Flask, render_template, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager


# create the app instance passing it the __name__ variable is used to set the name of the module
app = Flask(__name__)
# flask uses this location to figure out where certain files and folders are etc etc

app.config.from_object(Config)
# create an instance of my db
db = SQLAlchemy(app)
# create an instance of my migration engine
migrate = Migrate(app, db)

# from flask_login import LoginManager
# then create login = LoginManager(app)

# I think you may have recognised a theme here whenever I install a flask extensiom
# I create an instance of it in __init__.py
login = LoginManager(app)

from app import routes, models
