from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')

def app_world():
    return render_template('index.html')