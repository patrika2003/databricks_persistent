use javafs;
CREATE TABLE employee(
employee_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
department VARCHAR(50),
salary DECIMAL(10,2),
hire_date DATE
);

insert into employee values(1,'PATRIKA','CHATTERJEE','CSE',58000,'2003-07-29');
insert into employee values(2,'AKRITI','TRIPATHI','CSE',85000,'2003-07-10');

CREATE VIEW sales_employee AS
select employee_id,first_name,last_name,salary from employee where department='Sales';
select * from sales_employee;

CREATE INDEX idx_department ON EMPLOYEE(employee_id);