"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)

try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE DETAILS (customer_id char(50) PRIMARY KEY, company_name varchar(100) NOT NULL, contact_name varchar(50))")
            cur.execute("SELECT * FROM customers_data")
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()

try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE DETAILS (employee_id int PRIMARY KEY, first_name varchar(100) NOT NULL,\
	        last_name varchar(100), title text, birth_date date, notes text)")
            cur.execute("SELECT * FROM employees_data")
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()

try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE DETAILS (order_id int PRIMARY KEY,\
            customer_id varchar(5) REFERENCES customers_data(customer_id) NOT NULL,\
            employee_id integer REFERENCES employees_data(employee_id),\
        	order_date date, ship_city varchar(100))")
            cur.execute("SELECT * FROM orders_data")
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()




# \COPY customers_data FROM 'C:\Users\gurya\PycharmProjects\postgres-homeworks\homework-1\north_data\customers_data.csv' DELIMITER ',' CSV HEADER;
#
# \COPY employees_data FROM 'C:\Users\gurya\PycharmProjects\postgres-homeworks\homework-1\north_data\employees_data.csv' DELIMITER ',' CSV HEADER;
#
# \COPY orders_data FROM 'C:\Users\gurya\PycharmProjects\postgres-homeworks\homework-1\north_data\orders_data.csv' DELIMITER ',' CSV HEADER;

