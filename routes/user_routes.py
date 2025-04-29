from routes import app
from flask import render_template
@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")