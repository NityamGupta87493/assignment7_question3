from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure the MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nityam123",
    database="registration_info"
)

# Create a cursor for executing queries
cursor = db.cursor()

# Define the table creation function (only needed for initial setup)
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        mobile_number VARCHAR(15) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """)
    db.commit()

# Call the function to create the table
create_table()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    user_id = request.form['userId']
    mobile_number = request.form['mobileNumber']
    password = request.form['password']
    
    # Insert the user details into the database
    query = "INSERT INTO users (user_id, mobile_number, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, mobile_number, password))
    db.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
