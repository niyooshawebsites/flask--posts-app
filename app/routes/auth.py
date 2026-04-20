from flask import Blueprint, flash, redirect, render_template, request, url_for
from passlib.hash import sha256_crypt

# from app.extensions import mysql
from app.forms.register import RegisterForm
from app.forms.login import LoginForm
from app.models.user import create_user, login_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POSTS'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        db_user_password = login_user(email)
        
        if sha256_crypt.verify(password, db_user_password):
            pass
    return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.hash(form.password.data)

        create_user(name, email, username, password)

        flash("You are now registered and can login", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)
