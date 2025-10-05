-- SELECT * FROM customers;
SELECT * FROM products WHERE category = 'Drinks';
SELECT * FROM orders ORDER BY order_date DESC;

SELECT COUNT(*) AS total_orders FROM orders;
SELECT p.product_name, SUM(p.price * o.quantity) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;

SELECT AVG(price) AS average_price FROM products;

SELECT o.order_id, c.name AS customer, p.product_name, o.quantity, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;

SELECT c.name AS customer, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;SQL queries for retrieving insights
