from flask import Flask

app = Flask(__name__)

@app.route('/')

def app_world():
    return '<h5> Hello 123 world! </h5>'