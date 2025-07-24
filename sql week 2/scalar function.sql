CREATE TABLE students(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(40),
    email VARCHAR(20) UNIQUE
);
CREATE TABLE courses(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(20),
    course_length_weeks INT,
    credits INT
);
CREATE TABLE enrollments(
    course_id INT,
    student_id INT,
    grade INT,
    completion_status boolean,
    PRIMARY KEY(course_id, student_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE ON UPDATE CASCADE);
INSERT INTO students (student_id, student_name, email) VALUES
(1, 'Ananya', 'ananya@gmail.com'),
(2, 'Ravi', 'ravi@gmail.com'),
(3, 'Neha', 'neha@gmail.com');
INSERT INTO courses (course_id, course_name, course_length_weeks, credits) VALUES
(101, 'Python', 8, 4),
(102, 'DBMS', 6, 3),
(103, 'Java', 10, 5);
INSERT INTO enrollments (course_id, student_id, grade, completion_status) VALUES
(101, 1, 85, TRUE),
(102, 1, 90, TRUE),
(103, 2, 70, FALSE),
(102, 3, 88, TRUE);
UPDATE students
SET student_id = 10
WHERE student_id = 1;
-- UPDATE courses
-- SET course_id = 201
-- WHERE course_id = 101;

select * from students;
select * from courses;
select * from enrollments;

select ucase() from students;


select FORMAT(1234.1234,2) AS Format_Number;
select ROUND(1560.46744,2) AS Round_Value;