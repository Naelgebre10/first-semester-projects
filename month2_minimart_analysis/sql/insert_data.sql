-- INSERT INTO customers (name, email, join_date) VALUES
('Alice Johnson', 'alice@example.com', '2024-01-10'),
('Bob Smith', 'bob@example.com', '2024-02-05'),
('Charlie Kim', 'charlie@example.com', '2024-02-25'),
('Diana Lopez', 'diana@example.com', '2024-03-12'),
('Ethan Brown', 'ethan@example.com', '2024-03-20');

INSERT INTO products (product_name, category, price) VALUES
('Cola', 'Drinks', 10.00),
('Water', 'Drinks', 5.00),
('Bread', 'Bakery', 6.50),
('Milk', 'Dairy', 12.00),
('Eggs', 'Dairy', 8.00);

INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 3, '2024-04-01'),
(2, 3, 2, '2024-04-02'),
(3, 5, 1, '2024-04-02'),
(4, 2, 5, '2024-04-03'),
(5, 4, 2, '2024-04-03');SQL script to insert sample data
