create database subquery;
use subquery;

create table employees(
name varchar(50),
salary int);

insert into employees values('A',50000);
insert into employees values('B',70000);
insert into employees values('C',70000);
insert into employees values('D',60000);

select name,salary from employees where salary=(select max(salary) from employees);

