import sqlite3
with  sqlite3.connect("../db/school.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
    
    print("Database created and connected successfully.")
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Students(
                       student_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL UNIQUE,
                       age INTEGER,
                       major TEXT)""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL UNIQUE,
        instructor_name TEXT)""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students (student_id),
        FOREIGN KEY (course_id) REFERENCES Courses (course_id))""")
    
    print("Tables created successfully.")
    cursor.execute("INSERT OR IGNORE INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
    cursor.execute("INSERT OR IGNORE INTO Students (name, age, major) VALUES ('Bob', 22, 'History')") 
    cursor.execute("INSERT OR IGNORE INTO Students (name, age, major) VALUES ('Charlie', 19, 'Biology')") 
    
    cursor.execute("INSERT OR IGNORE INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
    cursor.execute("INSERT OR IGNORE INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')") 
    cursor.execute("INSERT OR IGNORE INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')")
    
    conn.commit()
    print("Sample data inserted successfully.")
    
    def add_student(cursor, name, age, major):
        
        try:
            cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

    def add_course(cursor, name, instructor):
        try:
            cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

    with sqlite3.connect("../db/school.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        cursor = conn.cursor()

    # Insert sample data into tables

    add_student(cursor, 'Alice', 20, 'Computer Science')  
    add_student(cursor, 'Bob', 22, 'History')
    add_student(cursor, 'Charlie', 19, 'Biology')
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Math 102', 'Dr. Ray')
    add_course(cursor, 'Math 103', 'Dr. Ray')
    add_course(cursor, 'Computer 101', 'Dr. Jobs')
    add_course(cursor, 'Computer 102', 'Dr. Jobs')
    

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")
    
    cursor.execute("SELECT * FROM Students")
    
    students = cursor.fetchall()

    # for student in students:
    #         print(student)
            
    cursor.execute("SELECT * FROM Courses")
    courses = cursor.fetchall()
    
    # for course in courses:
    #     print(course)

    # cursor.execute("SELECT name, student_id FROM Students WHERE age = 22 AND major = 'History'")
    # Smith = cursor.fetchall()
    # for course in Smith:
    #     print(course)
    
    # cursor.execute("PRAGMA database_list")
    # print("this")
    # print(cursor.fetchall())        
    add_student(cursor, 'Momo', 20, 'Computer Science') 
    conn.commit()
    cursor.execute("SELECT * FROM Students WHERE major = 'Computer Science'")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
    def enroll_student(cursor, student, course):
        cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
        results = cursor.fetchall()
        if len(results) > 0:
            student_id = results[0][0]
        else:
            print(f"There was no student named {student}.")
            return
        cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
        results = cursor.fetchall()
        if len(results) > 0:
            course_id = results[0][0]
        else:
            print(f"There was no course named {course}.")
            return
        
        cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"Student {student} is already enrolled in course {course}.")
            return
        
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

        # And at the bottom of your "with" block

    enroll_student(cursor, "Alice", "Math 101")
    enroll_student(cursor, "Alice", "Chemistry 101")
    enroll_student(cursor, "Bob", "Math 101")
    enroll_student(cursor, "Bob", "English 101")
    enroll_student(cursor, "Charlie", "English 101")
    enroll_student(cursor, "Momo", "Math 101")
    enroll_student(cursor, "Momo", "Computer 102")
    
    conn.commit()
    
    cursor.execute(""" SELECT Students.name, Courses.course_name 
                   FROM students 
                   JOIN Enrollments ON Students.student_id = Enrollments.student_id
                   JOIN Courses ON Enrollments.course_id = Courses.course_id""")
    results = cursor.fetchall()
    for row in results:
        print(row)
        