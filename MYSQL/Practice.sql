CREATE TABLE customer_accounts (
    account_id INT NOT NULL,
    customer_name VARCHAR(15) NOT NULL,
    email VARCHAR(30),
    join_date DATE,
    account_balance DECIMAL(10,2)
);

INSERT INTO customer_accounts VALUES 
(1, 'Alice Smith', 'alice@email.com', '2025-01-15', 250.00),
(2, 'Bob Jones', NULL, '2025-02-20', 10.50),
(3, 'Charlie Brown', 'charlie@email.com', '2025-03-01', 0.00),
(4, 'Diana Prince', NULL, '2025-05-12', 1500.00);

# To get the value
select * from customer_accounts;
