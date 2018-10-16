from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.models import User
from app import db

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    posts = []
    for userX in users:
        dictX = {}
        dictX['author'] = {'username': userX.username}
        dictX['height'] = userX.height
        dictX['width'] = userX.width
        posts.append(dictX)
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

@app.route('/error')
def error():
    nothing = 0

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.height = form.height.data
        user.width = form.width.data

        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
