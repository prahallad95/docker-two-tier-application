from flask import Flask, render_template, request
import mysql.connector
import time

app = Flask(__name__)

db_config = {
    "host": "mysql-db",
    "user": "root",
    "password": "root123",
    "database": "messagesdb"
}

def get_connection():
    while True:
        try:
            conn = mysql.connector.connect(**db_config)
            return conn
        except:
            print("Waiting for MySQL...")
            time.sleep(5)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        message = request.form["message"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO messages(message) VALUES(%s)",
            (message,)
        )

        conn.commit()
        conn.close()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")

    messages = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        messages=messages
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
