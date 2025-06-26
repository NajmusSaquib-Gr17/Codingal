CREATE TABLE Salesman(
    Salesman_id TEXT PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    City TEXT NOT NULL,
    Commission REAL
);

INSERT INTO Salesman(Salesman_id, Name, Email, City, Commission) VALUES
('S001', 'John Smith', 'john.smith@example.com', 'New York', 0.10),
('S002', 'Emily Davis', 'emily.davis@example.com', 'Los Angeles', 0.12),
('S003', 'Michael Brown', 'michael.brown@example.com', 'Chicago', 0.15),
('S004', 'Sarah Johnson', 'sarah.johnson@example.com', 'Houston', 0.11),
('S005', 'David Wilson', 'david.wilson@example.com', 'Miami', 0.09),
('S006', 'Sophia Martinez', 'sophia.martinez@example.com', 'Dallas', 0.14),
('S007', 'James Anderson', 'james.anderson@example.com', 'Seattle', 0.13),
('S008', 'Olivia Taylor', 'olivia.taylor@example.com', 'Boston', 0.12),
('S009', 'William Thomas', 'william.thomas@example.com', 'Denver', 0.10),
('S010', 'Isabella Moore', 'isabella.moore@example.com', 'San Francisco', 0.15);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders(
    Order_No TEXT PRIMARY KEY,
    Purchase_Amount REAL,
    Order_date TEXT,
    Customer_ID TEXT,
    Salesman_ID TEXT
);

INSERT INTO Orders(Order_No, Purchase_Amount, Order_date, Customer_ID, Salesman_ID) VALUES
('O1001', 2500.50, '2024-06-15', 'C001', 'S001'),
('O1002', 1800.00, '2024-06-18', 'C002', 'S002'),
('O1003', 3200.75, '2024-06-20', 'C003', 'S003'),
('O1004', 1500.25, '2024-06-22', 'C004', 'S001'),
('O1005', 2750.00, '2024-06-25', 'C005', 'S004'),
('O1006', 4000.00, '2024-06-26', 'C002', 'S002'),
('O1007', 2200.30, '2024-06-27', 'C006', 'S005'),
('O1008', 3100.00, '2024-06-28', 'C007', 'S006'),
('O1009', 2900.50, '2024-06-29', 'C008', 'S003'),
('O1010', 3500.00, '2024-06-30', 'C009', 'S007');

SELECT * FROM Orders;