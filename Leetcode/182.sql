Select email as Email
from Person
Group by email
having count(*) >1;