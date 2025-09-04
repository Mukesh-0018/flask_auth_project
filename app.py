from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = '4f273b951ca52803a406f1f5cab5c581'

#MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="wick#venTure18",
    database="flask_auth"
)
cursor = db.cursor()

#Register route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

#Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute("SELECT * FROM users WHERE username =%s AND password = %s", (username, password))
        result = cursor.fetchone()
        if user:
            session['username'] = username
            return redirect(url_for("welocme"))
        else:
            return "Invalid credentials"
    return render_template("login.html")

#Welcome route

@app.route("/welcome")
def welcome():
    if "username" in session:
        return render_templete("welcome.html", username = session["username"])
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
