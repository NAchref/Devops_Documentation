from dotenv import load_dotenv
from flask import Flask, render_template
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

# Pages Routes 
@app.route('/')
def index():
    return render_template('index.html')

