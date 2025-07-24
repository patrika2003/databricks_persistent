CREATE TABLE students (
 id INT PRIMARY KEY,
 name VARCHAR(50),
 age INT,
 gender VARCHAR(10),
 marks INT,
 city VARCHAR(50)
);
INSERT INTO students (id, name, age, gender, marks, city) VALUES
(1, 'Alice', 20, 'Female', 85, 'Delhi'),
(2, 'Bob', 22, 'Male', 67, 'Mumbai'),
(3, 'Charlie', 23, 'Male', 92, 'Delhi'),
(4, 'Daisy', 21, 'Female', 74, 'Kolkata'),
(5, 'Evan', 20, 'Male', 89, 'Chennai'),
(6, 'Fiona', 22, 'Female', 95, 'Mumbai');

SELECT name, age FROM students;
SELECT DISTINCT city FROM students;
SELECT * FROM students WHERE gender = 'Male';
SELECT * FROM students WHERE marks > 80;
SELECT * FROM students WHERE age BETWEEN 20 AND 22;
SELECT * FROM students WHERE city = 'Delhi';
SELECT * FROM students WHERE name LIKE 'A%';
SELECT * FROM students ORDER BY marks DESC;
SELECT * FROM students LIMIT 3;
SELECT COUNT(*) AS total_students FROM students;
SELECT AVG(marks) AS average_marks FROM students;
SELECT MAX(marks) AS highest_marks FROM students;
SELECT * FROM students ORDER BY age ASC LIMIT 1;
SELECT COUNT(DISTINCT city) AS unique_cities FROM students;
SELECT gender, COUNT(*) AS count FROM students GROUP BY gender;
SELECT city, AVG(marks) AS average_marks FROM students GROUP BY city;
SELECT gender, MAX(marks) AS top_marks FROM students GROUP BY gender;

