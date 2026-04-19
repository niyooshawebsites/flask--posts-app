from flask import Blueprint, flash, redirect, render_template, request, url_for
from passlib.hash import sha256_crypt

from app.extensions import mysql
from app.forms.register import RegisterForm
from app.models.user import create_user

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
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
