from flask import Blueprint, redirect, render_template, url_for, session

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def index():
    print(session)  # 👈 this will show everything in session
    if 'logged_in' in session:
        return render_template("dashboard/index.html")
    else:
        return redirect(url_for("auth.login"))