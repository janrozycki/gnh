from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

