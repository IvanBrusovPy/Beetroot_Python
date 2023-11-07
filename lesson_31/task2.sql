SELECT
    first_name as "First Name",
    last_name as "Last Name"
from employees

SELECT
    distinct department_id
from employees
order by department_id

select *
from employees
order by first_name desc

select
    first_name, last_name, salary, (salary*0.12) as "PF"
from employees


select
    max(salary) as "Max salary",
    min(salary) as "Min salary"
from employees
