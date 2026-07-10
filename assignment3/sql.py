import sqlite3

conn = sqlite3.connect("students.db")


def run_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def run_query_no_output(query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


# Create table
run_query_no_output("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    score REAL DEFAULT 0.0
);
""")

# Insert records
run_query_no_output("""
INSERT INTO students (name, course, score)
VALUES ('Rahul', 'Python', 85);
""")

run_query_no_output("""
INSERT INTO students (name, course, score)
VALUES ('Priya', 'SQL', 92);
""")

run_query_no_output("""
INSERT INTO students (name, course, score)
VALUES ('Aman', 'Data Science', 78);
""")

# Print all rows
rows = run_query("SELECT * FROM students;")

for row in rows:
    print(row)

conn.close()