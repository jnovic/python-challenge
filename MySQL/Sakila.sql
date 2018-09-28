USE SAKILA;
-- 1a 
Select first_name, .last_name from actor;
-- 1b
Select Upper(concat(first_name, " ", last_name)) as "Actor Name" from actor;

-- 2a
Select actor_id, first_name, last_name from actor
Where first_name like "Joe";
-- 2b
Select first_name, last_name from actor
Where last_name like "%GEN%"; 
-- 2c
Select last_name, first_name from actor
Where last_name like "%LI%";
-- 2d
select country_id, country from country
Where country in ("Afghanistan", "Bangladesh", "China");

-- 3a
alter table actor
add description blob;
-- 3b
alter table actor
drop description;

-- 4a
Select last_name, count(last_name) as "count" from actor
group by last_name;

-- 4b
Select last_name, count(last_name) as "count" from actor
group by last_name
having count(last_name) >1;

-- 4c
SET SQL_SAFE_UPDATES = 0;
update actor 
SET first_name = "HARPO"
WHERE first_name = "GROUCHO" and last_name = "WILLIAMS";

-- 4d
update actor
set first_name = "GROUCHO"
where first_name = "HARPO";

-- 5a
SHOW CREATE TABLE address;

-- 6a
Select staff.first_name, staff.last_name, address.address 
from staff 
join address 
on staff.address_id = address.address_id;

-- 6b
Select staff.first_name, staff.last_name, sum(payment.amount) as "amount rung"
from staff
join payment
on staff.staff_id = payment.staff_id
group by staff.staff_id;








