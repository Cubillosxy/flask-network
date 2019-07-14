from os.path import join
from datetime import datetime
import time

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm
from forms import RegistrationForm

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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default_img.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author',  lazy=True)

    def __repr__(self):
        return f'User: {self.username}, '


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'POST {self.id}, {self.title}'



mock_post = [
    {
        'author': 'Edwin C',
        'date': '02/10/2018',
        'title': 'first blog',
        'content': 'bla bla',
    },

    {
        'author': 'Vingo C',
        'date': '02/14/2018',
        'title': 'se blog',
        'content': 'blsd s da bla',
    },
]


def url_for_static(filename):
    root = app.config.get('STATIC_ROOT', '')
    return join(root, filename)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', data=mock_post)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "hola@gmail.com":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Pleaese !', 'danger')
    return render_template('login.html', title='Login', form=form)


def database_initialization_sequence():
    print('db init...')
    db.create_all()
    test_rec = User(
        username='edwinc',
        email='edwin@gmail.com',
        #'demo.jpg',
        password='demopass',
    )

    db.session.add(test_rec)
    db.session.rollback()
    print('db test complete. ')
    db.session.commit()


if __name__ == '__main__':
    dbstatus = False
    while dbstatus == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            dbstatus = True
    database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')
