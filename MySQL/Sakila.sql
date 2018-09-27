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





