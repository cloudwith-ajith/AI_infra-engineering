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
----------------------------------------primary key, check ,default,foreign key
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

---------indexs,view
create table student_info (
  id int not null primary key ,
  first_name varchar(25) not null,
  last_name varchar(20) not null,
  age int
);


insert into student_info values
(1,"Ajith","Kumar",23),
(2,"Ajay","Kumar",22),
(3,"Anil","Kumar",23),
(4,"Akash","Kumar",23);


select * from student_info;

--creating the index

create index id_index on student_info(id);


desc student_info;


----joins
create table student(
  id int not  null,
  first_name varchar(20),
  last_name varchar(20),
  age int 
);

insert into student values
(1,"Ajith","Kumar",18),
(2,"Anil","Kumar",18),
(3,"Akash","Kumar",18),
(4,"Amal","Kumar",18);


select * from student;


create table student_records (
  id int not null,
  department varchar(20),
  total_mark int,
  student_rank int 
);

insert into student_records values
(1,'CSE',499,1),
(3,'CSE',412,6),
(2,'EEE',409,15);

------------------------------------------inner join 

select * from student_records;
 
select * from student 
inner join student_records on student.id = student_records.id;

select a.id,a.first_name, a.last_name, b.department,b.total_mark,b.student_rank from student a 
inner join student_records b  on a.id = b.id;

Output:
+----+------------+-----------+------+
| id | first_name | last_name | age  |
+----+------------+-----------+------+
|  1 | Ajith      | Kumar     |   18 |
|  2 | Anil       | Kumar     |   18 |
|  3 | Akash      | Kumar     |   18 |
|  4 | Amal       | Kumar     |   18 |
+----+------------+-----------+------+
+----+------------+-----------+------------+------------+--------------+
| id | first_name | last_name | department | total_mark | student_rank |
+----+------------+-----------+------------+------------+--------------+
|  1 | Ajith      | Kumar     | CSE        |        499 |            1 |
|  3 | Akash      | Kumar     | CSE        |        412 |            6 |
|  2 | Anil       | Kumar     | EEE        |        409 |           15 |
+----+------------+-----------+------------+------------+--------------+

----------------------------------------left join 

select * from student
left join student_records on student.id = student_records.id;
Output:
+----+------------+-----------+------+
| id | first_name | last_name | age  |
+----+------------+-----------+------+
|  1 | Ajith      | Kumar     |   18 |
|  2 | Anil       | Kumar     |   18 |
|  3 | Akash      | Kumar     |   18 |
|  4 | Amal       | Kumar     |   18 |
+----+------------+-----------+------+
+----+------------+-----------+------+------+------------+------------+--------------+
| id | first_name | last_name | age  | id   | department | total_mark | student_rank |
+----+------------+-----------+------+------+------------+------------+--------------+
|  1 | Ajith      | Kumar     |   18 |    1 | CSE        |        499 |            1 |
|  2 | Anil       | Kumar     |   18 |    2 | EEE        |        409 |           15 |
|  3 | Akash      | Kumar     |   18 |    3 | CSE        |        412 |            6 |
|  4 | Amal       | Kumar     |   18 | NULL | NULL       |       NULL |         NULL |
+----+------------+-----------+------+------+------------+------------+--------------+
----------------------------------------right join

select * from student
right join student_records on student.id = student_records.id;
Output:
+----+------------+-----------+------+
| id | first_name | last_name | age  |
+----+------------+-----------+------+
|  1 | Ajith      | Kumar     |   18 |
|  2 | Anil       | Kumar     |   18 |
|  3 | Akash      | Kumar     |   18 |
|  4 | Amal       | Kumar     |   18 |
+----+------------+-----------+------+
+------+------------+-----------+------+----+------------+------------+--------------+
| id   | first_name | last_name | age  | id | department | total_mark | student_rank |
+------+------------+-----------+------+----+------------+------------+--------------+
|    1 | Ajith      | Kumar     |   18 |  1 | CSE        |        499 |            1 |
|    3 | Akash      | Kumar     |   18 |  3 | CSE        |        412 |            6 |
| NULL | NULL       | NULL      | NULL |  5 | BME        |        450 |            7 |
|    2 | Anil       | Kumar     |   18 |  2 | EEE        |        409 |           15 |
+------+------------+-----------+------+----+------------+------------+--------------+


----------------------------------------full outer join 
select * from student
left join student_records on student.id = student_records.id
union
select * from student
right join student_records on student.id = student_records.id;

Output:
+----+------------+-----------+------+
| id | first_name | last_name | age  |
+----+------------+-----------+------+
|  1 | Ajith      | Kumar     |   18 |
|  2 | Anil       | Kumar     |   18 |
|  3 | Akash      | Kumar     |   18 |
|  4 | Amal       | Kumar     |   18 |
+----+------------+-----------+------+
+------+------------+-----------+------+------+------------+------------+--------------+
| id   | first_name | last_name | age  | id   | department | total_mark | student_rank |
+------+------------+-----------+------+------+------------+------------+--------------+
|    1 | Ajith      | Kumar     |   18 |    1 | CSE        |        499 |            1 |
|    2 | Anil       | Kumar     |   18 |    2 | EEE        |        409 |           15 |
|    3 | Akash      | Kumar     |   18 |    3 | CSE        |        412 |            6 |
|    4 | Amal       | Kumar     |   18 | NULL | NULL       |       NULL |         NULL |
| NULL | NULL       | NULL      | NULL |    5 | BME        |        450 |            7 |
+------+------------+-----------+------+------+------------+------------+--------------+

---------------------------------------- cross join


select * from student
cross join student_records;


Output:
+----+------------+-----------+------+
| id | first_name | last_name | age  |
+----+------------+-----------+------+
|  1 | Ajith      | Kumar     |   18 |
|  2 | Anil       | Kumar     |   18 |
|  3 | Akash      | Kumar     |   18 |
|  4 | Amal       | Kumar     |   18 |
+----+------------+-----------+------+
+----+------------+-----------+------+----+------------+------------+--------------+
| id | first_name | last_name | age  | id | department | total_mark | student_rank |
+----+------------+-----------+------+----+------------+------------+--------------+
|  4 | Amal       | Kumar     |   18 |  1 | CSE        |        499 |            1 |
|  3 | Akash      | Kumar     |   18 |  1 | CSE        |        499 |            1 |
|  2 | Anil       | Kumar     |   18 |  1 | CSE        |        499 |            1 |
|  1 | Ajith      | Kumar     |   18 |  1 | CSE        |        499 |            1 |
|  4 | Amal       | Kumar     |   18 |  3 | CSE        |        412 |            6 |
|  3 | Akash      | Kumar     |   18 |  3 | CSE        |        412 |            6 |
|  2 | Anil       | Kumar     |   18 |  3 | CSE        |        412 |            6 |
|  1 | Ajith      | Kumar     |   18 |  3 | CSE        |        412 |            6 |
|  4 | Amal       | Kumar     |   18 |  5 | BME        |        450 |            7 |
|  3 | Akash      | Kumar     |   18 |  5 | BME        |        450 |            7 |
|  2 | Anil       | Kumar     |   18 |  5 | BME        |        450 |            7 |
|  1 | Ajith      | Kumar     |   18 |  5 | BME        |        450 |            7 |
|  4 | Amal       | Kumar     |   18 |  2 | EEE        |        409 |           15 |
|  3 | Akash      | Kumar     |   18 |  2 | EEE        |        409 |           15 |
|  2 | Anil       | Kumar     |   18 |  2 | EEE        |        409 |           15 |
|  1 | Ajith      | Kumar     |   18 |  2 | EEE        |        409 |           15 |
+----+------------+-----------+------+----+------------+------------+--------------+



--------interview prep
create database company;

show databases;

use company;

create table employee(
emp_id int not null auto_increment,
first_name varchar(15) not null,
last_name varchar(10),
salary varchar(6),
join_date datetime default current_timestamp,
department varchar(10),
primary key(emp_id)
);


INSERT INTO employee (first_name, last_name, salary, join_date, department) VALUES 
('Amit', 'Sharma', '85000', '2022-03-15 09:00:00', 'Sales'),
('Priya', 'Patel', '95000', '2021-06-01 10:30:00', 'Admin'),
('Rahul', 'Verma', '70000', '2023-01-10 14:15:00', 'HR'),
('Sneha', 'Reddy', '65000', '2022-11-20 11:00:00', 'Sales'),
('Vikram', 'Singh', '30000', '2024-05-01 09:30:00', 'Admin'),
('Rohan', 'Das', '72000', '2023-08-14 16:45:00', 'HR');

#-- These rows omit join_date and last_name to test your table's DEFAULT and NULL capabilities
INSERT INTO employee (first_name, last_name, salary, department) VALUES 
('Ananya', 'Mishra', '88000', 'Sales'),
('Karan', NULL, '45000', 'Admin');

select * from employee;

create table bonus(
emp_id int not null,
bonus_date date,
bonus_amount int,
foreign key (emp_id) references employee(emp_id)
);

INSERT INTO bonus (emp_id, bonus_date, bonus_amount) VALUES 
(1, '2023-12-25', 5000),  -- Amit (Sales)
(2, '2023-12-25', 7000),  -- Priya (Admin)
(3, '2023-12-25', 4000),  -- Rahul (HR)
(1, '2024-06-15', 3500),  -- Amit gets a second bonus
(4, '2023-12-25', 4500),  -- Sneha (Sales)
(7, '2024-01-01', 6000);  -- Ananya (Sales)

select * from bonus;

select * from employee
left join bonus on employee.emp_id = bonus.emp_id;

create table designation(
des_id int not null,
designation varchar(15),
designation_date date,
foreign key (des_id)references employee(emp_id)
);
INSERT INTO designation (des_id, designation, designation_date) VALUES 
(1, 'Manager', '2022-03-15'),      -- Amit
(2, 'Lead Developer', '2021-06-01'),-- Priya
(3, 'HR Specialist', '2023-01-10'), -- Rahul
(4, 'Executive', '2022-11-20'),     -- Sneha
(5, 'Intern', '2024-05-01'),        -- Vikram
(6, 'Analyst', '2023-08-14'),       -- Rohan
(7, 'Senior Manager', '2024-02-01');-- Ananya

-- Employee 8 (Karan) is left without a designation row to help you practice NULL handling joins.
select * from designation
