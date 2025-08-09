CREATE TABLE Customers (
    CustID INT PRIMARY KEY,
    Name VARCHAR(50),
    Country VARCHAR(50)
);

CREATE TABLE Products (
    ProdID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10,2)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustID INT,
    ProdID INT,
    Quantity INT,
    FOREIGN KEY (CustID) REFERENCES Customers(CustID),
    FOREIGN KEY (ProdID) REFERENCES Products(ProdID)
);

INSERT INTO Customers (CustID, Name, Country)
VALUES
(1, 'Alice', 'USA'),
(2, 'Aaron', 'UK'),
(3, 'George', 'Canada'),
(4, 'Morris', 'Australia'),
(5, 'Amora', 'Germany'),
(6, 'Victor', 'USA');

INSERT INTO Products (ProdID, ProductName, Price)
VALUES
(101, 'Laptop', 750.00),
(102, 'Smartphone', 500.00),
(103, 'Tablet', 300.00),
(104, 'Headphones', 80.00),
(105, 'Monitor', 200.00);

INSERT INTO Orders (OrderID, CustID, ProdID, Quantity)
VALUES
(1001, 1, 101, 2),
(1002, 2, 103, 1),
(1003, 3, 104, 3),
(1004, 4, 105, 2),
(1005, 5, 102, 5),
(1006, 6, 101, 1);

SELECT * FROM Customers
WHERE Name LIKE 'a%';

SELECT * FROM Customers
WHERE Name LIKE '%or%';

SELECT DISTINCT Country
FROM Customers;

SELECT c.Name AS CustomerName,
       c.Country,
       p.ProductName,
       o.Quantity,
       (p.Price * o.Quantity) AS TotalValue
FROM Customers c
JOIN Orders o ON c.CustID = o.CustID
JOIN Products p ON o.ProdID = p.ProdID
ORDER BY TotalValue DESC;

SELECT c.Country,
       SUM(p.Price * o.Quantity) AS TotalSales
FROM Customers c
JOIN Orders o ON c.CustID = o.CustID
JOIN Products p ON o.ProdID = p.ProdID
GROUP BY c.Country
HAVING SUM(p.Price * o.Quantity) > 500
ORDER BY TotalSales DESC;