-- SQL-команды для создания таблиц
CREATE DATABASE north
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE customers_data
(
	customer_id char(50) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(50)
);

CREATE TABLE employees_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100),
	title text,
	birth_date date,
	notes text
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers_data(customer_id) NOT NULL,
	employee_id integer REFERENCES employees_data(employee_id),
	order_date date,
	ship_city varchar(100)
);