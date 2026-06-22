SELECT firstname, lastname, city, state
From Person
Left join address
On Person.personId = Address.personid;