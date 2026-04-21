from flask import Blueprint, flash, redirect, render_template, request, url_for, session
from passlib.hash import sha256_crypt
from app.forms.register import RegisterForm
from app.forms.login import LoginForm
from app.models.user import create_user, login_user

auth = Blueprint("auth", __name__)

# login
@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        db_user_password = login_user(username)
        if(db_user_password):
            if sha256_crypt.verify(password, db_user_password):
                session['logged_in'] = True
                session['username'] = username
                
                flash("You are now logged in", "success")
                return redirect(url_for("dashboard.index"))
            else:
                error = "Invalid Credentials"
                return render_template("login.html", form=form, error=error)
        else:
            error = "Invalid Credentials"
            return render_template("login.html", form=form, error=error)
    else:
        return render_template("login.html", form=form)
    
# logout   
@auth.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    flash('You are now logged out.', 'success')
    return redirect(url_for("auth.login"))

# register
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
