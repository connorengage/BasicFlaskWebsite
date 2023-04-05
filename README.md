**Basic Python/Flask website template with a HTML banner for navigating pages.**

I have imported Flask, and use pipenv for the virtual enviornment. Chose Python 3.11.2 code interpreter.


```
My directory:
.
├── Pipfile
├── Pipfile.lock
├── __pycache__
│   └── pages.cpython-311.pyc
├── app.py
├── pages.py
├── static
│   └── logo.png
└── templates
    ├── base.html
    ├── home.html
    ├── page1.html
    ├── page2.html
    ├── team.html
    └── contact.html
```
### ----------------------

## static folder:
logo.png - a basic placeholder logo

### ----------------------

## pages.py: where I define all of my flask routes
```
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
```

## app.py:---
```
from flask import Flask
from pages import pages


app = Flask(__name__)
app.register_blueprint(pages, url_prefix="/")
if __name__ == '__main__':
    app.run(debug=True, port=8000)
```
## ----------------------

**Inside the templates folder my HTML:**

## base.html: the banner---
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Default Title{% endblock %}</title>
    <style>
        .navbar {
            display: flex;
            justify-content: space-around;
            align-items: center;
            background-image: linear-gradient(to right, #f0f0f0, #007bff);
            padding: 1rem;
        }

        .navbar a {
            text-decoration: none;
            color: #333;
            font-size: 1.1rem;
            font-weight: bold;
            margin: 0 1rem;
        }

        .navbar a:hover {
            color: #fff;
        }

        .logo {
            height: 60px;
            margin-right: 1rem;
        }
    </style>
</head>
<body>
    <div class="navbar">
        <img class="logo" src="{{ url_for('static', filename='logo.png') }}" alt="Logo">
        <a href="/home">HOME</a>
        <a href="/page1">PAGE 1</a>
        <a href="/page2">PAGE 2</a>
        <a href="/team">TEAM</a>
        <a href="/contact">CONTACT</a>
    </div>

    {% block content %}
    {% endblock %}
</body>
</html>
```

## home.html:---
```
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Company</h1>
{% endblock %}
```

## page1.html:---
```
{% extends "base.html" %}

{% block title %}Page 1{% endblock %}

{% block content %}
    <h1>Company</h1>
    <h1>PAGE 1</h1>
{% endblock %}
```

## page2.html:---
```
{% extends "base.html" %}

{% block title %}Page 2{% endblock %}

{% block content %}
    <h1>Company</h1>
    <h1>PAGE 2</h1>
{% endblock %}
```

## team.html:---
```
{% extends "base.html" %}

{% block title %}Team{% endblock %}

{% block content %}
    <h1>Company</h1>
    <h1>Meet the team:</h1>
{% endblock %}
```

## contact.html:---
```
{% extends "base.html" %}

{% block title %}Contact{% endblock %}

{% block content %}
    <h1>Company</h1>
    <h1>Contact us:</h1>
{% endblock %}
```
## ---------------------- 
