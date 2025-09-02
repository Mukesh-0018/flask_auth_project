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