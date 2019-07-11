from os.path import join

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '95b54bbdcb40a3e4ef9fcc3de57ca763'

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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
