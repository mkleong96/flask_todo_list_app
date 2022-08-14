from http.client import HTTPResponse
import os

from flask import Flask, jsonify, redirect, render_template, url_for, request
from flask_dance.contrib.github import github
from flask_login import logout_user, login_required

from app.models import db, login_manager
from app.oauth import github_blueprint 

import sqlite3

#Flask app initialization
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'OOC1L7kTpayyulSxyuwnKA'
app.register_blueprint(github_blueprint, url_prefix="/login")
db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()

#API
@app.route("/ping")
def ping():
    if github.authorized:
        return github.get("/user").json()
    return jsonify(ping="not authenticated")

@app.route("/")
def homepage():
    provider       = None 
    social_account = None
    
    if github.authorized:
        print(github.authorized)
        social_account = github.get("/user").json()['html_url']
        provider       = 'Github' 
    return render_template("index.html", social_account=social_account, provider=provider)

@app.route("/login/github")
def login_github():
    if not github.authorized:
        return redirect(url_for("github.login"))
    res = github.get("/user")
    username = res.json()["login"]
    return f"You are @{username} on GitHub"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/list_all")
def list_all():
    conn_db = sqlite3.connect('users.db')
    cursor = conn_db.cursor()
    statement = "SELECT * from to_do_list"
    cursor.execute(statement)
    output = cursor.fetchall()
    return str(output)

@app.route("/add_to_do_list", methods = ['POST'])
def add_list():
    title = request.json['title']
    description = request.json['description']
    status = request.json['status']
    conn_db = sqlite3.connect('users.db')
    data = (None, title, description, status)
    conn_db.execute("INSERT INTO to_do_list VALUES(?, ?, ? ,?)", data)
    conn_db.commit()
    return "New to-do list added"

@app.route("/delete_list", methods = ['POST'])
def delete_list():
    id = request.json['id']
    conn_db = sqlite3.connect('users.db')
    cursor = conn_db.cursor()
    sql_update_query = """DELETE FROM to_do_list WHERE id = ?"""
    cursor.execute(sql_update_query, (id,))
    conn_db.commit()
    return "To do list deleted"

@app.route("/mark_list_done", methods = ['POST'])
def mark_list_done(): 
    id = request.json['id']
    status = request.json['status']
    conn_db = sqlite3.connect('users.db')
    cursor = conn_db.cursor()
    sql_update_query = """UPDATE to_do_list SET complete_status =? WHERE id = ?"""
    data = (status, id)
    cursor.execute(sql_update_query, data)
    conn_db.commit()
    return "To do list updated"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
