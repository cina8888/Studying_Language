select name As Employee
from Employee e
where salary > (select salary from Employee m where e.ManagerID = m.id);