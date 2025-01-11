from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL connection
db_config = {
    "host": os.getenv("MYSQL_HOST", "mysql"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "your_root_password"),
    "database": os.getenv("MYSQL_DATABASE", "testdb")
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# Create
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data["name"], data["email"]))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User added successfully"}), 201

# Read
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

# Update
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (data["name"], data["email"], user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User updated successfully"})

# Delete
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User deleted successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

