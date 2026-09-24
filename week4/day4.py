import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade INTEGER
        )
    """)
    conn.commit()
    conn.close()


@app.route("/students")
def list_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    students = [dict(row) for row in rows]
    return jsonify(students)


@app.route("/students/count")
def students_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()
    conn.close()
    return jsonify({"count": count[0]})


@app.route("/students/average")
def students_average():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(grade) FROM students")
    avg = cursor.fetchone()
    conn.close()
    if avg[0] is None:
        return jsonify({"average": 0})
    return jsonify({"average": avg[0]})


@app.route("/students/above/<int:min_grade>")
def mingrade_of_students(min_grade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE grade > ?", (min_grade,))
    rows = cursor.fetchall()
    conn.close()
    students = [dict(row) for row in rows]
    return jsonify(students)


@app.route("/students/<name>", methods=["GET", "DELETE", "PUT"])
def search_student(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "DELETE":
        cursor.execute("DELETE FROM students WHERE name = ?", (name,))
        conn.commit()
        conn.close()
        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404
        return jsonify({"message": f"{name} deleted"})

    elif request.method == "PUT":
        data = request.get_json()
        new_grade = data["grade"]
        cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, name))
        conn.commit()
        conn.close()
        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404
        return jsonify({"message": f"{name}'s grade updated to {new_grade}"})

    else:
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return jsonify(dict(row))
        return jsonify({"error": "Student not found"}), 404


@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.get_json()
    if not data.get("name") or not data.get("grade"):
        return jsonify({"message": "Student name or grade is missing"}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (data["name"], data["grade"]))
    conn.commit()
    conn.close()
    return jsonify(data), 201


if __name__ == "__main__":
    init_db()
    app.run(debug=True)