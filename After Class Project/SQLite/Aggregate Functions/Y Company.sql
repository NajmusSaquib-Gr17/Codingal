CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10,2)
);

INSERT INTO Employees (EmpID, Name, Department, Salary)
VALUES
(1, 'Ravi', 'IT', 55000.00),
(2, 'Amit', 'Finance', 60000.00),
(3, 'Rohit', 'HR', 50000.00),
(4, 'Pooja', 'IT', 65000.00),
(5, 'Neha', 'Finance', 62000.00),
(6, 'Raj', 'IT', 70000.00);

SELECT SUM(Salary) AS TotalSalary
FROM Employees;

SELECT AVG(Salary) AS AverageSalary
FROM Employees;

SELECT COUNT(DISTINCT Department) AS TotalDepartments
FROM Employees;

SELECT MIN(Salary) AS MinimumSalary
FROM Employees;

SELECT MAX(Salary) AS MaximumSalary
FROM Employees;