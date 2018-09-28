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

-- 6c
select film.title, count(film_actor.actor_id) as "Actor Movie Count"
from film_actor
inner join film
on film_actor.film_id = film.film_id
group by film.film_id
;

-- 6d
SELECT Count(inventory_id) as "Total Copies of Hunchback Impossible"
FROM inventory
Where film_id IN
(
SELECT film_id
FROM film
WHERE title = 'Hunchback Impossible'
    );
    
-- 6e
Select customer.last_name, customer.first_name, sum(payment.amount) as "Total Amount Paid"
from customer
join payment
on customer.customer_id = payment.customer_id
group by customer.customer_id
order by customer.last_name;

-- 7a
Select film.title 
from film
where title like "K%" or "Q%" and language_id in
(select language_id
from language
where name = "English");

-- 7b
Select first_name, last_name 
from actor
where actor_id in
(select actor_id
from film_actor
where film_id in
(select film_id 
from film
where title = "Alone Trip"
));

-- 7c
select customer.first_name, customer.last_name, address.address, city.city, address.district, country.country, address.postal_code
from customer
join address
on customer.address_id = address.address_id
join city
on address.city_id = city.city_id
join country
on city.country_id = country.country_id
where country.country = "Canada";

-- 7d
select title 
from film
where film_id in
(select film_id 
from film_category
where category_id in
(select category_id
from category
where name = "Family"
));

-- 7e













