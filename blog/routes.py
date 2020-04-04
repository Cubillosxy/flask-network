# routes
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask import request
from flask import abort
from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required
from sqlalchemy import or_

from blog.forms import LoginForm
from blog.forms import RegistrationForm
from blog.forms import AccountForm
from blog.forms import PostForm


from blog.models import User
from blog.models import Post
from blog.utils import save_picture

from blog import app
from blog import db
from blog import bcrypt


def url_for_static(filename):
    root = app.config.get('STATIC_ROOT', '')
    return join(root, filename)


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


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
        if form.picture.data:
            img_file = save_picture(form.picture.data)
            user.image_file = img_file
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

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            img_file = save_picture(form.picture.data)
            current_user.image_file = img_file
        current_user.email = form.email.data
        current_user.username = form.username.data
        db.session.commit()
        flash('Account Update', 'success')
        return redirect(url_for('account'))

    image_file = url_for('static', filename='profile_img/{}'.format(current_user.image_file))
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash('Account Update', 'success')
        return redirect(url_for('home'))
    return render_template(
        'new_post.html', 
        title='New Post', 
        form=form,
        legend='New Post'
    )

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', title=post.title, post=post)


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post update', 'success')
        return redirect(url_for('post_detail', post_id=post_id))

    # implici GET
    form.title.data = post.title
    form.content.data = post.content 
    return render_template(
        'new_post.html', 
        title='Update Post',  
        form=form,
        legend='Update Post'
    )
