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

-------DAY3
show databases;

use student;

show tables;
select * from student_info;

create table Instagram_login(
id integer not null,
user_name varchar(15) not null,
email varchar(20) not null,
age integer,
phone_number integer,
sex varchar(8));

select * from Instagram_login;

alter table Instagram_login
modify phone_number varchar(10);

insert into Instagram_login values 
(1,"ajith","ajith@gmail.com",null,8220419685,"male"),
(2,"vijay","vijay@gmail.com",31,null,"male");

show tables;

desc instagram_login;

#unique

alter table instagram_login
add unique(id);

alter table instagram_login
add unique(phone_number);

alter table instagram_login
add  constraint pk_key primary key(id,phone_number);
----------------------------------------primary key, check ,default
create table user(
  user_id int not null primary key,
  first_name varchar(20) not null,
  last_name varchar(20),
  account_balance int,
  age int check(age >= 18),
  join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

insert into user(user_id,first_name,last_name,account_balance,age) values
  (1,"Ajith","kumar",99, 23),
  (2,"Shamini","s", 340,19);


select * from user
---------------------------------------primary key, foreign key
CREATE TABLE user(
  user_id INT NOT NULL PRIMARY KEY,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20),
  account_balance INT,
  age INT,
  join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Removed the extra outer parentheses here
INSERT INTO user(user_id, first_name, last_name, account_balance, age) VALUES 
  (1, "Ajith", "kumar", 99, 23),
  (2, "Shamini", "s", 340, 21);

SELECT * FROM user;

create table user(
  user_id int not null primary key,
  first_name varchar(20) not null,
  last_name varchar(20),
  account_balance int,
  age int check(age >= 18),
  join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

insert into user(user_id,first_name,last_name,account_balance,age) values
  (1,"Ajith","kumar",99, 23),
  (2,"Shamini","s", 340,19);


select * from user


create table user(
  id int not null primary key auto_increment,
  first_name varchar(20),
  last_name varchar(20),
  salary int,
  age int,
  join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  constraint Age_voliation check(age >= 18)
);

insert into user( first_name,last_name,salary,age) values 
("Ajith","kumar",123,23),
("shamini","s",90000,18);

select * from user;

