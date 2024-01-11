from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os

from flask_sqlalchemy import SQLAlchemy

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

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    add_task_to_database(title, description)
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    try:
        with db_connection.cursor() as cursor:
            sql = "DELETE FROM tasks WHERE id = %s"
            cursor.execute(sql, (task_id,))
            db_connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db_connection.rollback()
    return redirect(url_for('index'))