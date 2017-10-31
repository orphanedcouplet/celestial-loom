from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime


app = Flask(__name__)
app.config["DEBUG"] = True
# # Note: the connection string after :// contains the following info:
# # user:password@server:portNumber/databaseName
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://blogz:blogzdev@localhost:8889/blogz"
# app.config["SQLALCHEMY_ECHO"] = True
# db = SQLAlchemy(app)
# app.secret_key = "fldkslfakljfkdlsjaksfvnxclzxnfeowafdjsk49urt0mklfsda"

# TODO define classes, if any, for db, if i need a db

@app.route("/", methods=["POST", "GET"])
def show_page():
    page_title = "Fellowship of the Incarnate Divine"
    return render_template("index.html", page_title=page_title)

if __name__ == "__main__":
    app.run()
