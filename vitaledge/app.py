from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For session management

# Database connection
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        problem TEXT UNIQUE,
        recommended_action TEXT
    )""")

    # Sample medical problems
    sample_data = [
        ("Headache", "Take paracetamol and drink water."),
        ("Fever", "Stay hydrated and take ibuprofen."),
        ("Chest Pain", "Seek immediate medical attention."),
        ("Sprain", "Apply ice and rest the limb."),
        ("Cough", "Drink warm fluids and use cough syrup."),
    ]

    for problem, action in sample_data:
        cursor.execute("INSERT OR IGNORE INTO problems (problem, recommended_action) VALUES (?, ?)", (problem.lower(), action))
    
    conn.commit()
    conn.close()

init_db()  # Run database initialization

# Homepage (Login / Register)
@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

# Register Route
@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    except sqlite3.IntegrityError:
        return "Username already exists!"

# Login Route
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        session["username"] = username
        return redirect(url_for("dashboard"))
    else:
        return "Invalid credentials"

# Logout Route
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

# Dashboard (User Logged In)
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("dashboard.html", username=session["username"])

# First-Aid Check Route
@app.route("/first_aid", methods=["POST"])
def first_aid():
    problem = request.form["problem"].strip().lower()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT recommended_action FROM problems WHERE problem LIKE ?", ('%' + problem + '%',))
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({"action": result["recommended_action"]})
    else:
        return jsonify({"action": "Problem not found. Please consult a doctor."})

if __name__ == "__main__":
    app.run(debug=True)
