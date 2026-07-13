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

# challenges1 --- to get the null value form the table,
--behind the scence, it scan email caloumns, row by row,
--found the empty memory placeholder and return the values

select * from customer_accounts
where email is null;

--use the update the value, best thing is we need to add the values to the
--existin values
update customer_accounts set account_balance =  account_balance + 50.00 
where account_id = 3;

select * from customer_accounts;


Delete from customer_accounts
where account_id = 2;

select * from customer_accounts;

--for create the new columns and ading the value as the active

ALTER TABLE customer_accounts
ADD COLUMN account_status VARCHAR(10) DEFAULT 'active';

SELECT * FROM customer_accounts;
