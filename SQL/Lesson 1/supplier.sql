CREATE TABLE supplier(
    S_no INT PRIMARY KEY,
    S_name VARCHAR(20),
    Status TEXT,
    City TEXT
);

INSERT INTO supplier(S_no, S_name, Status, City) VALUES
(1, 'Supplier1', 'Active', 'New York'),
(2, 'Supplier2', 'Inactive', 'Los Angeles'),
(3, 'Supplier3', 'Active', 'Chicago'),
(4, 'Supplier4', 'Active', 'Houston'),
(5, 'Supplier5', 'Inactive', 'Miami'),
(6, 'Supplier6', 'Active', 'Dallas'),
(7, 'Supplier7', 'Active', 'San Francisco'),
(8, 'Supplier8', 'Inactive', 'Seattle'),
(9, 'Supplier9', 'Active', 'Boston'),
(10, 'Supplier10', 'Active', 'Denver');

SELECT * FROM supplier;
