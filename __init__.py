from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from flask_assets import Bundle, Environment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd51404d77d44f9257992e8c48d8311d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'signin' #signin is the page were login_required decorator is going to look for the information. video: 6 time 39:59
login_manager.login_message_catogory = 'info'


#assets = Environment(app)
##js = Bundle('profile.js', output='gen/main.js')
##assets.register('main.js', js)

from feedo import routes

# debugger pin: 238-026-771
