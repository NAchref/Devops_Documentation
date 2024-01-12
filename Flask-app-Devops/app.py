from dotenv import load_dotenv
from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
import pymysql

# Load environment variables
load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

# Set SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

# Enable SQLAlchemy track modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Initialize SQLAlchemy
db = SQLAlchemy()
db.init_app(app)


# Database connection info with environment variables
db_connection = pymysql.connect(
    host=os.environ.get('DB_HOST', 'localhost'),
    user=os.environ.get('DB_USER', 'root'),
    password=os.environ.get('DB_PASSWORD', 'password'),
    database=os.environ.get('DB_DATABASE', 'todo_db'),
    cursorclass=pymysql.cursors.DictCursor
)


# Pages Routes 
@app.route('/')
def index():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

