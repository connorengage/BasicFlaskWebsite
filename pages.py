from flask import Blueprint, render_template, request, jsonify, redirect, url_for

pages = Blueprint("pages", __name__)

@pages.route("/")
def landing():
    return render_template("index.html")

@pages.route("/home")
def home():
    return redirect(url_for("pages.landing"))

@pages.route("/page1")
def page1():
    return render_template("page1.html")

@pages.route("/page2")
def page2():
    return render_template("page2.html")

@pages.route("/team")
def team():
    return render_template("team.html")

@pages.route("/contact")
def contact():
    return render_template("contact.html")