from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


# ----------------------------
# CORS
# ----------------------------
@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
    return response


# ----------------------------
# GET ALL STUDENTS
# ----------------------------
@app.route("/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    students = []

    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "course": row[3]
        })

    conn.close()

    return jsonify(students)


# ----------------------------
# GET ONE STUDENT
# ----------------------------
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        student = {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "course": row[3]
        }
        return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


# ----------------------------
# ADD STUDENT
# ----------------------------
@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (
            data["name"],
            data["age"],
            data["course"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student added successfully"
    }), 201


# ----------------------------
# UPDATE STUDENT
# ----------------------------
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET name = ?, age = ?, course = ?
        WHERE id = ?
        """,
        (
            data["name"],
            data["age"],
            data["course"],
            id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student updated successfully"
    })


# ----------------------------
# DELETE STUDENT
# ----------------------------
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student deleted successfully"
    })


# ----------------------------
# DASHBOARD API
# ----------------------------
@app.route("/api/dashboard", methods=["GET", "OPTIONS"])
def get_dashboard():

    if request.method == "OPTIONS":
        return "", 204

    return jsonify({
        "overview": {
            "average_assessment_score": "78.54",
            "average_feedback_score": "4.13",
            "total_attendees": 507,
            "total_completions": 468,
            "total_planned_participants": 543,
            "total_sessions": 20,
            "total_training_cost": "605000.00"
        },
        "monthly_trend": [],
        "category_breakdown": [],
        "recent_sessions": [],
        "status": "ok"
    })


# ----------------------------
# RUN APP
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)

