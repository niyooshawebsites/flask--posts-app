from flask import Blueprint, flash, redirect, render_template, url_for, session, request
from app.forms.post import PostForm
from app.models.post import create_post, fetch_all_posts, delete_single_post, fetch_single_post, edit_article

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
    
@dashboard.route("/delete/post/<int:id>", methods=['GET'])
def delPost(id):
    if "logged_in" in session:
        deletedPost = delete_single_post(id)
        if deletedPost:
            flash('Post deleted successfully', "success")
            return redirect(url_for("dashboard.index"))
        else:
            flash("Failed to delete the post", "danger")
            return redirect(url_for("dashboard.index"))
    else:
        flash("Unauthorized. Please login")
        return redirect(url_for("auth.login"))
    
@dashboard.route("/edit/post/<int:id>", methods=['GET', 'POST'])
def editPost(id):
    if 'logged_in' in session:
        post = fetch_single_post(id)  # fetch existing post

        if not post:
            flash("Post not found", "danger")
            return redirect(url_for("dashboard.index"))

        form = PostForm(request.form)

        if request.method == 'POST' and form.validate():
            title = form.title.data
            content = form.content.data

            edit_article(id, title, content)
            flash("Post updated successfully", "success")
            return redirect(url_for("dashboard.index"))

        else:
            form.title.data = post['title']
            form.content.data = post['content']
            return render_template("dashboard/edit.html", form=form)

    else:
        flash("Unauthorized! Please login!", "danger")
        return redirect(url_for("auth.login"))

