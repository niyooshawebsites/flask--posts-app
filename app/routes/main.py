from flask import Blueprint, render_template
from app.models.post import fetch_all_posts, fetch_single_post

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/posts")
def posts():
    posts = fetch_all_posts()
    return render_template("posts.html", posts=posts)


@main.route("/post/<int:id>")
def post(id):
    post = fetch_single_post(id)
    return render_template("post.html", post=post)
