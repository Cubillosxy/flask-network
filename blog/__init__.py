
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


DBUSER = 'postgres'
DBPASS = 'foobarbaz'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'postgres'


#DBUSER = 'flask'
#DBPASS = 'flaskpass'
#DBNAME = 'flask_db'


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
    user=DBUSER,
    passwd=DBPASS,
    host=DBHOST,
    port=DBPORT,
    db=DBNAME
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '95b54bbdcb40a3e4ef9fcc3de57ca763'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from blog import routes