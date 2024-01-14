from dotenv import load_dotenv
from flask import Flask, render_template
import os

from flask_sqlalchemy import SQLAlchemy
import psycopg2

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



# Function to establish a database connection
def get_database_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None 





# Pages Routes 
@app.route('/')
def index():
    return render_template('index.html')

