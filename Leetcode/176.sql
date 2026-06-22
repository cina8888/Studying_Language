Select (
    Select distinct salary
    FROM employee
    Order by salary DESC
    Limit 1 offset 1
)AS SecondHighestSalary;
