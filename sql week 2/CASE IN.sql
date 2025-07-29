-- case in
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT
);
INSERT INTO employees (id, name, salary) VALUES
(1, 'Alice', 80000),
(2, 'Bob', 60000),
(3, 'Charlie', 45000),
(4, 'Diana', 72000),
(5, 'Evan', 50000),
(6, 'Fay', 30000);


SELECT name,salary,
	CASE
		when SALARY>=70000 THEN 'High'
		when salary BETWEEN 50000 AND 69999 THEN 'Medium'
		ELSE 'Low'
	END AS salary_level
FROM employees;

select * from employees ORDER BY 
CASE department 
	WHEN 'IT' THEN 1 
	WHEN 'HR' THEN 2 ELSE 3
END;

UPDATE employees 
SET salary=
CASE
WHEN department='IT' THEN salary+5000
WHEN department='HR' THEN salary+2000
ELSE salary