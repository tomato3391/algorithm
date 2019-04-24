# Write a SQL query to get the second highest salary from the Employee table.

# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+

select case count(distinct(Salary)) when '0' then null else Salary end as SecondHighestSalary from (select Salary from Employee where Salary < (select max(Salary) from Employee) order by -Salary limit 1)a
