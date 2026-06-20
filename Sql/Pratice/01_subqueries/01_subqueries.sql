 /* Using a subquery, find the highest-paid employee(s)
*/
Select emp_name, salary
from Employees
where salary = (select max(salary) from Employees);
/*
Display employee names who work in departments
where the average salary is greater than 5500
*/
select
	emp_id,
	emp_name
from employees
where dept_id in
(
select
	dept_id
from employees
group by dept_id
having avg(salary) > 5500);

/*
Write a query to display employee names
who work in departments where
the average salary is greater than 6000.
*/
select
	emp_name
from employees
where dept_id in(

select
	dept_id
from employees
group by dept_id
having avg(salary) > 6000);
/*
Display employee names who work in departments
where the maximum salary is greater than 7000.
*/
select
	emp_name
from employees
where dept_id in (
select
	dept_id
from employees
group by dept_id
having max(salary) > 7000);
/*
Display department names
where at least one employee earns more than Sam.
*/
select dept_name
from Departments
where dept_id in 
(select dept_id 
from Employees 
where salary > (select salary from Employees where emp_name = 'Sam')
group by dept_id);

/* Show the employee names
who earn more than Mia
*/
Select emp_name
from Employees
Where salary > (select salary from Employees where emp_name = 'Mia');


/*
Display department names
where no one earns more than Mia.
*/
select dept_name
from Departments
where dept_id not in 
(select dept_id
from Employees
where salary > (select salary from Employees where emp_name  = 'Mia'));

/*
Display employee names
whose salary is not less than anyone in IT department
*/
select emp_name
from Employees
where salary >= 
(select min(salary) 
from Employees 
where dept_id = 
(select dept_id 
from Departments 
where dept_name = 'IT'));
/*
Display employee names
whose salary is greater than or equal to
the highest salary in HR department.
*/

/*Display employee names
whose salary is greater than or equal to
the average salary in Finance department.
*/

/* 
Display employee names
whose salary is less than
the highest salary in the Marketing department.
*/

/* Display employee names
whose salary is equal to
the minimum salary in the HR department.
*/

/*
Display employee names
whose salary is NOT equal to
the highest salary in the IT department.
*/

/* Display employee names
whose salary is not equal to
the minimum salary in the Finance department.
*/

/* Display employee names
whose salary is equal to
the maximum salary in the department where David works.
*/

/*
Display department names
where the average salary is less than Grace’s salary.
*/

/*
Display department names
where the maximum salary
is greater than Grace’s salary.
*/

/*
Display department names
where the minimum salary
is less than Grace’s salary.
*/

/*
Display department names
where the average salary
is equal to the average salary
of the Sales department.
*/

/*
Display employee names
who belong to a department that exists in the Departments table.
*/

