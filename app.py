from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Connect to Railway MySQL
conn = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database",
    port=your_port
)

@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    
    if result:
        return "✅ Login Successful!"
    else:
        return "❌ Invalid Credentials"

if __name__ == '__main__':
    app.run(debug=True)
