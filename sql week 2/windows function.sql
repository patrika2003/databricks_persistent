CREATE TABLE sales(
emp_id INT,
department CHAR,
amount INT,
sale_date date
);
INSERT INTO sales(emp_id,department,amount,sale_date) VALUES(1,"A",100,'2024-01-01');
INSERT INTO sales(emp_id,department,amount,sale_date) VALUES(2,"A",200,'2024-01-02');
INSERT INTO sales(emp_id,department,amount,sale_date) VALUES(3,"B",300,'2024-01-01');
INSERT INTO sales(emp_id,department,amount,sale_date) VALUES(4,"A",100,'2024-01-02');
SELECT * FROM sales;
SELECT emp_id, department, amount,
     ROW_NUMBER() OVER (PARTITION BY department ORDER BY amount DESC) AS row_num
FROM sales;
 
SELECT emp_id, department, amount,
     RANK() OVER (PARTITION BY department ORDER BY amount DESC) AS ran , 
     DENSE_RANK() OVER (PARTITION BY department ORDER BY amount DESC) AS dense_ran from Sales;
     
	SELECT emp_id, department, amount,
     SUM(amount) OVER (PARTITION BY department) AS dept_total
FROM sales;

SELECT emp_id, amount,
     LAG(amount) OVER (ORDER BY sale_date) AS prev_amount,
     LEAD(amount) OVER (ORDER BY sale_date) AS next_amount
FROM sales;

SELECT emp_id, department, amount,
     FIRST_VALUE(amount) OVER (PARTITION BY department ORDER BY sale_date) AS first_sale,
     LAST_VALUE(amount) OVER (PARTITION BY department ORDER BY sale_date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_sale
FROM sales;

select emp_id,amount,NTILE(2) OVER (ORDER BY amount) As bucket from Sales;
 
