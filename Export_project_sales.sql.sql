-- 0. Fresh database for export practice
DROP DATABASE IF EXISTS export_project;
CREATE DATABASE export_project;
USE export_project;

-- 1. create tables 
DROP TABLE IF EXISTS order_item;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
   customer_id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
   city VARCHAR(100)
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_item (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT DEFAULT 1,
    price DECIMAL(10,2) DEFAULT 0.00,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 2. Insert sample data (safe small dataset)
INSERT INTO customers (name, city) VALUES
('Aman','Delhi'),
('Ravi','Mumbai'),
('Sita','Kolkata'),
('Rahul','Delhi'),
('NoOrder','Chennai');

INSERT INTO products (product_name, category, price) VALUES 
('Notebook','Stationery',50.00),
('Pen','Stationery',10.00),
('Mouse','Electronics',500.00),
('Keyboard','Electronics',800.00),
('T-Shirt','Apparel',299.00);

-- Orders
INSERT INTO orders (customer_id, order_date) VALUES
(1,'2025-11-20'),
(1,'2025-11-25'),
(2,'2025-10-10'),
(3,'2025-09-15');

-- Orders items (use same product price; stored again to allow price)
INSERT INTO order_item (order_id, product_id, quantity, price) VALUES 
(1,1,2,50.00),
(1,2,5,10.00),
(2,3,1,500.00),
(3,3,2,450.00),
(3,4,1,800.00),
(4,5,3,299.00);

SELECT
  p.product_id,
  p.product_name,
  p.category,
  COALESCE(SUM(oi.quantity * oi.price), 0) AS total_sales,
  COALESCE(SUM(oi.quantity), 0) AS total_quantity_sold
FROM products p
LEFT JOIN order_item oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_sales DESC;

SELECT
  DATE_FORMAT(o.order_date, '%Y-%m') AS month,
  COALESCE(SUM(oi.quantity * oi.price), 0) AS monthly_revenue
FROM orders o
LEFT JOIN order_item oi ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;

SELECT
  c.customer_id,
  c.name AS customer_name,
  COUNT(DISTINCT o.order_id) AS total_orders,
  COALESCE(SUM(oi.quantity * oi.price), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN order_item oi ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 50;

SHOW VARIABLES LIKE 'secure_file_priv';

SELECT 
    p.product_id,
    p.product_name,
    p.category,
    COALESCE(SUM(oi.quantity * oi.price), 0) AS total_sales,
    COALESCE(SUM(oi.quantity), 0) AS total_quantity_sold
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/product_sales.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM products p
LEFT JOIN order_item oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_sales DESC;

-- raws counts 
SELECT COUNT(*) AS customers_count FROM customers;
SELECT COUNT(*) AS products_count FROM products;
SELECT COUNT(*) AS orders_count FROM orders;
SELECT COUNT(*) AS order_item_count FROM order_item;

USE export_project;
SELECT
  p.product_id,
  p.product_name,
  p.category,
  COALESCE(SUM(oi.quantity * oi.price), 0) AS total_sales,
  COALESCE(SUM(oi.quantity), 0) AS total_quantity_sold
FROM products p
LEFT JOIN order_item oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_sales DESC;
