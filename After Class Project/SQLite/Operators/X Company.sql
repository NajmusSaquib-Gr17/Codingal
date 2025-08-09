CREATE TABLE Customers (
    CustID INT PRIMARY KEY,
    Name VARCHAR(50),
    City VARCHAR(50),
    Grade INT
);

INSERT INTO Customers (CustID, Name, City, Grade)
VALUES
(1, 'John', 'New York', 120),
(2, 'David', 'Chicago', 95),
(3, 'Sophia', 'New York', 90),
(4, 'Emma', 'Boston', 110),
(5, 'Michael', 'New York', 130),
(6, 'Olivia', 'Los Angeles', 105);

SELECT * FROM Customers
WHERE City = 'New York' OR Grade > 100;

SELECT * FROM Customers
WHERE City = 'New York' AND Grade > 100;
