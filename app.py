from flask import Flask, render_template, request, redirect, url_for

from data.cereal_db import DbTool
from parsers.query_parser import parse_query

app = Flask(__name__)

db = DbTool()
current_user = None

@app.route('/', methods=["GET"])
def home():
    if 'search' in request.args:
        return render_template(
            "home.html",
            cereals=db.get_query_cereals(
                parse_query(
                    request.args['search']),
                    request.args['category']
                )
        )
    return render_template(
        "home.html",
        cereals=db.get_cereals()
    )

@app.route('/<int:id>')
def get_cereal_id(id):
    return render_template(
        "home.html",
        cereals=[db.get_cereal(id)]
    )

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if db.attempt_login(request.form['username'], request.form['password']):
            return "Logged in"
        return "tucked in"