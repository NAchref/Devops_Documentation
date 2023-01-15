from flask import Flask, render_template
import os

app = Flask(__name__)


# Pages Routes 
@app.route('/')
def index():
    return render_template('index.html')