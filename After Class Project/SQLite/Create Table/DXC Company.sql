CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10,2),
    Status VARCHAR(20)
);

INSERT INTO Employees (EmpID, Name, Department, Salary, Status)
VALUES
(1, 'Tarun', 'IT', 55000.00, 'Active'),
(2, 'Amit', 'Finance', 60000.00, 'Fraud'),
(3, 'Rohit', 'HR', 50000.00, 'Active'),
(4, 'Pooja', 'IT', 65000.00, 'Fraud'),
(5, 'Neha', 'Finance', 62000.00, 'Fraud'),
(6, 'Raj', 'IT', 70000.00, 'Active');

SELECT * FROM Employees
WHERE Status = 'Fraud';
SELECT Name, Department
FROM Employees
WHERE Status = 'Fraud';
