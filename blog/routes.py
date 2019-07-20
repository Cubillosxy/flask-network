# routes
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask import request
from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required
from sqlalchemy import or_

from .forms import LoginForm
from .forms import RegistrationForm


from .models import User
from .models import Post

from . import app
from . import db
from . import bcrypt

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
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pass_encrypt = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        username = form.username.data

        user = User(
            username=username,
            email=form.email.data,
            password=pass_encrypt,
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        #username = form.username.data
        email = form.email.data
        #user = User.query.filter(or_(User.username == username, User.email == email)).first()
        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login Unsuccessful invalid password', 'danger')
        else:
            flash('Login Unsuccessful. Invalid data !', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['GET'])
@login_required
def account():
    return render_template('account.html', title='Account')
