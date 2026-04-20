from flask import Blueprint, redirect, render_template, request, url_for, session

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def index():
    if session.get('logged_in'):
        return render_template("dashboard/index.html", usrname=session.get('username'))
    else:
        return redirect(url_for("auth.login"))