CREATE TABLE employees2025 (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INT
);
INSERT INTO employees2025 (emp_id, name, department, salary) VALUES
(1, 'Alice', 'IT', 80000),
(2, 'Bob', 'HR', 60000),
(3, 'Charlie', 'Finance', 50000),
(4, 'Diana', 'IT', 72000),
(5, 'Evan', 'Marketing', 45000);

SELECT name, department,
      CASE department
          WHEN 'IT' THEN 'Technology'
          WHEN 'HR' THEN 'People'
          ELSE 'Others'
      END AS dept_category
FROM employees2025;

WITH it_employees2025 AS (
   SELECT emp_id, name
   FROM employees2025
   WHERE department = 'IT'
),
salaries AS (
   SELECT emp_id, salary
   FROM employees2025
)
SELECT it.name, s.salary
FROM it_employees2025 it
JOIN salaries s ON it.emp_id = s.emp_id;

