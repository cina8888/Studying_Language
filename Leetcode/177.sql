CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
  RETURN (
        Select DistincT Salary
        From Employee
        Order by salary DESC
        Limit 1 OFFSET N