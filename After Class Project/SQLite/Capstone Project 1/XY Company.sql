CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Designation VARCHAR(50),
    Salary DECIMAL(10,2),
    City VARCHAR(50)
);

INSERT INTO Employees (EmpID, Name, Department, Designation, Salary, City)
VALUES
(1, 'Ravi', 'IT', 'Developer', 55000.00, 'Delhi'),
(2, 'Amit', 'Finance', 'Analyst', 60000.00, 'Mumbai'),
(3, 'Rohit', 'HR', 'Manager', 50000.00, 'Delhi'),
(4, 'Pooja', 'IT', 'Team Lead', 65000.00, 'Bangalore'),
(5, 'Neha', 'Finance', 'Manager', 62000.00, 'Pune'),
(6, 'Raj', 'IT', 'Architect', 70000.00, 'Delhi');


SELECT * FROM Employees;

UPDATE Employees
SET Salary = 75000.00
WHERE Name = 'Raj';

DELETE FROM Employees
WHERE Name = 'Rohit';


SELECT * FROM Employees
ORDER BY Salary DESC;


SELECT * FROM Employees
WHERE City = 'Delhi' AND Salary > 60000;

SELECT Department, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Department;


SELECT MAX(Salary) AS HighestSalary, MIN(Salary) AS LowestSalary
FROM Employees;