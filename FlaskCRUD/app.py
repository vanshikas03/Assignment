from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "training.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return "Student CRUD API"


@app.route("/students", methods=["POST"])
def create_student():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    required = ["name", "age", "course"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    conn = get_db()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
        (data["name"], data["age"], data["course"])
    )

    conn.commit()

    student_id = cursor.lastrowid

    conn.close()

    return jsonify({"message": "Student added", "id": student_id}), 201


@app.route("/students", methods=["GET"])
def get_students():

    conn = get_db()

    students = conn.execute("SELECT * FROM students").fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    conn = get_db()

    student = conn.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({"message": "Not found"}), 404

    return jsonify(dict(student))


@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    conn = get_db()

    conn.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (data["name"], data["age"], data["course"], id)
    )

    conn.commit()

    conn.close()

    return jsonify({"message": "Student updated"})


@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()

    conn.close()

    return jsonify({"message": "Student deleted"})


if __name__ == "__main__":
    app.run(debug=True)
