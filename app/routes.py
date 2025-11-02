from flask import Blueprint, render_template, redirect, url_for, request, flash, session, current_app
from app.models import User
from .forms import LoginForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            return redirect(url_for('main.dashboard'))
    return render_template('login.html',form=form)

@main.route('/dashboard', methods=['GET','POST'])
def dashboard():
    form = LoginForm()

    if form.exit.data:
        return redirect(url_for('main.login'))
    return render_template('dashboard.html',form=form)