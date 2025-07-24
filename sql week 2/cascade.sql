CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100)
);
 
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    -- ON DELETE CASCADE
    ON UPDATE CASCADE
);
 
-- Insert into customers
INSERT INTO customers VALUES (1, 'Remya'), (2, 'Aravind');
 
-- Insert into orders
INSERT INTO orders VALUES (101, 1, 'Laptop'), (102, 1, 'Phone'), (103, 2, 'Tablet');
select * from customers;
select * from orders;
-- DELETE FROM customers WHERE customer_id = 1;
select * from orders;
UPDATE customers
SET customer_id = 10
WHERE customer_id = 1;



 