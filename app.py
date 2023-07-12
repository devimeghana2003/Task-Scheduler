from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Devi@1234',
    'database': 'task_scheduler'
}

# Connect to the MySQL database
def connect_to_database():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/', methods=['GET'])
def index():
    conn = connect_to_database()
    cursor = conn.cursor()

    # Retrieve tasks from the database
    query = 'SELECT * FROM tasks'
    cursor.execute(query)
    tasks = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create_task():
    task_name = request.form['name']
    task_description = request.form['description']

    conn = connect_to_database()
    cursor = conn.cursor()

    # Insert the task into the database
    query = 'INSERT INTO tasks (name, description) VALUES (%s, %s)'
    values = (task_name, task_description)
    cursor.execute(query, values)
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    return 'Task created successfully'

if __name__ == '__main__':
    app.run(debug=True)

