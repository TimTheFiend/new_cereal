from flask import Flask, render_template, request, redirect, url_for

from data.cereal_db import DbTool

app = Flask(__name__)

db = DbTool()


@app.route('/')
def home():
    if 'search' in request.args:
        return render_template(
            "home.html",
            cereals=[db.get_cereal(int(request.args['search']))]
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
