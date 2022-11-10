from flask import Flask, render_template, request, redirect, url_for, session

from data.cereal_db import DbTool
from parsers.query_parser import parse_query, parse_advanced_query

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = DbTool()


@app.route('/', methods=["GET"])
def home():
    if session.get('login'):
        print(session['login'] == True)
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
            session['login'] = True
            return redirect(url_for('home'))
        return "tucked in"


@app.route('/logout')
def logout():
    if session['login'] == True:
        session['login'] = False
    return redirect(url_for('home'))


@app.route("/update", methods=["GET", "POST"])
def update():
    if not session.get('login') or session['login'] == False:
        return redirect(url_for('home'))
    if request.method == "GET":
        return render_template('update.html')
    elif request.method == "POST":
        if db.on_update(request.form):
            return redirect(url_for('home'))
        return "Something went wrong."


@app.route('/delete', methods=['GET','POST'])
def delete():
    if not session.get('login') or session['login'] == False:
        return redirect(url_for('home'))
    if request.method == "GET":
        return render_template('delete.html')
    elif request.method == 'POST':
        db.delete_cereal(request.form['id'])
        return redirect(url_for('home'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        queries = parse_advanced_query(request.form)
        cereal_box = db.get_query_cereals(queries)
        if cereal_box is None:
            return render_template(
            'home.html'
        )
        return render_template(
            'home.html',
            cereals=db.get_query_cereals(queries)
        )
    elif request.method == 'GET':
        return render_template(
            'search.html'
        )