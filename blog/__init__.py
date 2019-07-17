
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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

from blog import routes