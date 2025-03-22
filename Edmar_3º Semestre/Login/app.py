from flask import flask, render_template, request, redirect, session
import bcrypt
from config import get_db_connection

app = Flask (__name__)
app.secret_key = "segredo"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode("utf-8")
        hashed = bcrypt.hashpw( password, bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, password) VALUES(%s, %s)",(username, hashed))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/")
return render_template("register.html")