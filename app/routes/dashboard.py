from flask import Blueprint, flash, redirect, render_template, url_for, session, request
from app.forms.post import PostForm
from app.models.post import create_post, fetch_all_posts

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def index():
    if 'logged_in' in session:
        posts = fetch_all_posts()
        return render_template("dashboard/index.html", posts=posts)
    else:
        flash("Unauthorized! Please login!", "danger")
        return redirect(url_for("auth.login"))
    
@dashboard.route("/post/add", methods=['GET', 'POST'])
def addPost():
    if 'logged_in' in session:
        form = PostForm(request.form)
        if request.method == 'POST' and form.validate():
            title = form.title.data
            content = form.content.data 
            create_post(title, content, session['username'])
            flash("Post created successfully", "success")
            return redirect(url_for("dashboard.addPost"))
        else:
            return render_template("dashboard/add.html", form=form)
    else:
        flash("Unauthorized! Please login!", "danger")
        return redirect(url_for("auth.login"))

