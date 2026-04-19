from flask import Blueprint, render_template

from data import get_articles

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


@main.route("/articles")
def articles():
    articles = get_articles()
    return render_template("articles.html", articles=articles)


@main.route("/article/<int:id>")
def article(id):
    return render_template("article.html", id=id)
