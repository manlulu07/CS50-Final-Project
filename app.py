import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

app = Flask(__name__)

db = SQL("sqlite:///databases.db")
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response




@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET","POST"])
def login():

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("login.html")
        


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("username required")
        elif not password:
            return apology("password required")
        elif not confirmation:
            return apology("confirmation required")
        if password != confirmation:
            return apology("passwords do not match")

        hash = generate_password_hash(password)

        try:

            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",username,hash)
            return redirect("/login")
        except:
            return apology("username already exists")
    else:
        return render_template("register.html")

    
@app.route("/code")
@login_required
def code():
    return render_template("code.html")

@app.route("/schematic")
@login_required
def schematic():
    return render_template("schematic.html")

@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/")








