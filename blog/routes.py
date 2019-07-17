# routes
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for

from .forms import LoginForm
from .forms import RegistrationForm


from .models import User
from .models import Post

from . import app

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