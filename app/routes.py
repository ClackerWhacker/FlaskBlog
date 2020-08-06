import time

from flask_login import current_user, login_user, logout_user

from app import app, db

from flask import flash, render_template, redirect, url_for, request
from app.forms import LoginForm, Details, Registration
from app.models import Person


@app.route("/signup")
def signup():
    return "you do not have an account"

@app.route('/user/<username>')
def profile(username):
    user = Person.query.filter_by(name=username).first_or_404()
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Registration()
    if form.validate_on_submit():
        user = Person(name=form.username.data, email=form.email.data)
        user.create_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a new user")
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")

    form = LoginForm()

    if form.validate_on_submit():
        user = Person.query.filter_by(name=form.email.data).first()
        if user is None:
            flash("You do not have an account with us!")
            return redirect(url_for("register"))
        if not user.check_password(form.password.data):
            flash("Wrong password")
            return redirect(url_for("login"))
        flash("Corret password. Welcome.")
        login_user(user, remember=False)
        return redirect("/")

    return render_template("login1.html", form=form)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/details", methods=["GET", "POST"])
def details():
    detail = Details()
    if detail.validate_on_submit():
        print("Working")
        flash("Success")
        return redirect("https://www.facebook.com")

    return render_template("details.html", form=detail)
