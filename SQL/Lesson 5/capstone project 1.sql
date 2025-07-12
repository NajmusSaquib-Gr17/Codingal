CREATE TABLE IF NOT EXISTS Salesman(
    Salesman_ID TEXT PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    City TEXT,
    Commission TEXT NOT NULL
);

INSERT INTO Salesman(Salesman_ID, Name, Email, City, Commission) VALUES
('S001', 'Rahim Uddin', 'rahim.uddin@example.com', 'Dhaka', '10%'),
('S002', 'Karim Hasan', 'karim.hasan@example.com', 'Chittagong', '12%'),
('S003', 'Nasima Akter', 'nasima.akter@example.com', 'Rajshahi', '11%'),
('S004', 'Jamal Hossain', 'jamal.hossain@example.com', 'Sylhet', '9%'),
('S005', 'Ayesha Siddika', 'ayesha.siddika@example.com', 'Khulna', '13%'),
('S006', 'Badrul Alam', 'badrul.alam@example.com', 'Barisal', '10%'),
('S007', 'Salma Khatun', 'salma.khatun@example.com', 'Rangpur', '11%'),
('S008', 'Rezaul Karim', 'rezaul.karim@example.com', 'Mymensingh', '12%'),
('S009', 'Tania Rahman', 'tania.rahman@example.com', 'Comilla', '8%'),
('S010', 'Mamun Chowdhury', 'mamun.chowdhury@example.com', 'Gazipur', '14%'),
('S011', 'Sabbir Ahmed', 'sabbir.ahmed@example.com', 'Narayanganj', '10%'),
('S012', 'Nusrat Jahan', 'nusrat.jahan@example.com', 'Bogra', '9%'),
('S013', 'Faisal Mahmud', 'faisal.mahmud@example.com', 'Noakhali', '11%'),
('S014', 'Shila Rani Das', 'shila.das@example.com', 'Jessore', '13%'),
('S015', 'Tanvir Islam', 'tanvir.islam@example.com', 'Pabna', '10%'),
('S016', 'Mehzabin Chowdhury', 'mehzabin.c@example.com', 'Chandpur', '12%'),
('S017', 'Rashedul Hasan', 'rashedul.hasan@example.com', 'Kushtia', '9%'),
('S018', 'Farzana Kabir', 'farzana.kabir@example.com', 'Dinajpur', '8%'),
('S019', 'Jahirul Islam', 'jahirul.islam@example.com', 'Tangail', '11%'),
('S020', 'Lubna Sultana', 'lubna.sultana@example.com', 'Feni', '10%');

CREATE TABLE IF NOT EXISTS Customer(
    Customer_ID TEXT PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    City TEXT,
    Salesman_ID TEXT
);

INSERT INTO Customer(Customer_ID, Name, Email, City, Salesman_ID) VALUES
('C001', 'Abul Kalam', 'abul.kalam@example.com', 'Dhaka', 'S001'),
('C002', 'Rokeya Begum', 'rokeya.begum@example.com', 'Dhaka', 'S001'),
('C003', 'Selim Reza', 'selim.reza@example.com', 'Chittagong', 'S002'),
('C004', 'Minara Khatun', 'minara.khatun@example.com', 'Chittagong', 'S002'),
('C005', 'Shahidul Islam', 'shahidul.islam@example.com', 'Rajshahi', 'S003'),
('C006', 'Nasrin Sultana', 'nasrin.sultana@example.com', 'Rajshahi', 'S003'),
('C007', 'Kamal Hossain', 'kamal.hossain@example.com', 'Sylhet', 'S004'),
('C008', 'Aklima Begum', 'aklima.begum@example.com', 'Sylhet', 'S004'),
('C009', 'Mamun Mia', 'mamun.mia@example.com', 'Khulna', 'S005'),
('C010', 'Lamia Chowdhury', 'lamia.chowdhury@example.com', 'Khulna', 'S005'),
('C011', 'Ashraful Islam', 'ashraful.islam@example.com', 'Barisal', 'S006'),
('C012', 'Ruma Akter', 'ruma.akter@example.com', 'Barisal', 'S006'),
('C013', 'Mahbub Hossain', 'mahbub.hossain@example.com', 'Rangpur', 'S007'),
('C014', 'Tania Akter', 'tania.akter@example.com', 'Rangpur', 'S007'),
('C015', 'Faruk Ahmed', 'faruk.ahmed@example.com', 'Mymensingh', 'S008'),
('C016', 'Sharmin Nahar', 'sharmin.nahar@example.com', 'Mymensingh', 'S008'),
('C017', 'Jamil Uddin', 'jamil.uddin@example.com', 'Comilla', 'S009'),
('C018', 'Sabina Yasmin', 'sabina.yasmin@example.com', 'Comilla', 'S009'),
('C019', 'Tanvir Hossain', 'tanvir.hossain@example.com', 'Gazipur', 'S010'),
('C020', 'Mahira Islam', 'mahira.islam@example.com', 'Gazipur', 'S010'),
('C021', 'Habib Rahman', 'habib.rahman@example.com', 'Narayanganj', 'S011'),
('C022', 'Sumaiya Rahman', 'sumaiya.rahman@example.com', 'Narayanganj', 'S011'),
('C023', 'Hasan Mahmud', 'hasan.mahmud@example.com', 'Bogra', 'S012'),
('C024', 'Naznin Akter', 'naznin.akter@example.com', 'Bogra', 'S012'),
('C025', 'Mokhlesur Rahman', 'mokhlesur.rahman@example.com', 'Noakhali', 'S013'),
('C026', 'Papia Khatun', 'papia.khatun@example.com', 'Noakhali', 'S013'),
('C027', 'Rashed Mia', 'rashed.mia@example.com', 'Jessore', 'S014'),
('C028', 'Faria Sultana', 'faria.sultana@example.com', 'Jessore', 'S014'),
('C029', 'Asif Hossain', 'asif.hossain@example.com', 'Pabna', 'S015'),
('C030', 'Nadia Ahmed', 'nadia.ahmed@example.com', 'Pabna', 'S015'),
('C031', 'Rafiul Hasan', 'rafiul.hasan@example.com', 'Chandpur', 'S016'),
('C032', 'Mim Akter', 'mim.akter@example.com', 'Chandpur', 'S016'),
('C033', 'Shahadat Hossain', 'shahadat.hossain@example.com', 'Kushtia', 'S017'),
('C034', 'Rina Begum', 'rina.begum@example.com', 'Kushtia', 'S017'),
('C035', 'Rubel Mia', 'rubel.mia@example.com', 'Dinajpur', 'S018'),
('C036', 'Maliha Tasnim', 'maliha.tasnim@example.com', 'Dinajpur', 'S018'),
('C037', 'Shuvo Roy', 'shuvo.roy@example.com', 'Tangail', 'S019'),
('C038', 'Eliza Chowdhury', 'eliza.chowdhury@example.com', 'Tangail', 'S019'),
('C039', 'Saiful Islam', 'saiful.islam@example.com', 'Feni', 'S020'),
('C040', 'Sadia Sultana', 'sadia.sultana@example.com', 'Feni', 'S020'),
('C041', 'Babul Mia', 'babul.mia@example.com', 'Dhaka', 'S001'),
('C042', 'Nishi Akter', 'nishi.akter@example.com', 'Dhaka', 'S001'),
('C043', 'Liton Das', 'liton.das@example.com', 'Sylhet', 'S004'),
('C044', 'Mursalin Ahmed', 'mursalin.ahmed@example.com', 'Sylhet', 'S004'),
('C045', 'Zakia Jahan', 'zakia.jahan@example.com', 'Khulna', 'S005'),
('C046', 'Imran Hossain', 'imran.hossain@example.com', 'Khulna', 'S005'),
('C047', 'Munira Islam', 'munira.islam@example.com', 'Mymensingh', 'S008'),
('C048', 'Fahim Reza', 'fahim.reza@example.com', 'Comilla', 'S009'),
('C049', 'Tariqul Islam', 'tariqul.islam@example.com', 'Noakhali', 'S013'),
('C050', 'Nilufa Yasmin', 'nilufa.yasmin@example.com', 'Gazipur', 'S010');

CREATE TABLE IF NOT EXISTS Orders(
    Order_No TEXT PRIMARY KEY,
    Purchase_Amount TEXT NOT NULL,
    Order_Date TEXT NOT NULL,
    Customer_ID TEXT,
    Salesman_ID TEXT
);

INSERT INTO Orders(Order_No, Purchase_Amount, Order_Date, Customer_ID, Salesman_ID) VALUES
('O001', '15000', '2025-07-01', 'C001', 'S001'),
('O002', '22000', '2025-07-02', 'C002', 'S001'),
('O003', '18000', '2025-07-03', 'C003', 'S002'),
('O004', '25000', '2025-07-04', 'C004', 'S002'),
('O005', '12000', '2025-07-04', 'C005', 'S003'),
('O006', '16000', '2025-07-05', 'C006', 'S003'),
('O007', '21000', '2025-07-06', 'C007', 'S004'),
('O008', '17000', '2025-07-06', 'C008', 'S004'),
('O009', '13000', '2025-07-07', 'C009', 'S005'),
('O010', '14500', '2025-07-08', 'C010', 'S005'),
('O011', '19500', '2025-07-09', 'C011', 'S006'),
('O012', '23000', '2025-07-10', 'C012', 'S006'),
('O013', '14000', '2025-07-11', 'C013', 'S007'),
('O014', '18500', '2025-07-11', 'C014', 'S007'),
('O015', '20000', '2025-07-12', 'C015', 'S008'),
('O016', '21500', '2025-07-12', 'C016', 'S008'),
('O017', '15500', '2025-07-13', 'C017', 'S009'),
('O018', '16500', '2025-07-13', 'C018', 'S009'),
('O019', '17500', '2025-07-14', 'C019', 'S010'),
('O020', '20500', '2025-07-14', 'C020', 'S010'),
('O021', '19000', '2025-07-15', 'C021', 'S011'),
('O022', '22000', '2025-07-15', 'C022', 'S011'),
('O023', '13500', '2025-07-16', 'C023', 'S012'),
('O024', '18000', '2025-07-16', 'C024', 'S012'),
('O025', '24000', '2025-07-17', 'C025', 'S013'),
('O026', '20000', '2025-07-17', 'C026', 'S013'),
('O027', '18500', '2025-07-18', 'C027', 'S014'),
('O028', '21000', '2025-07-18', 'C028', 'S014'),
('O029', '16500', '2025-07-19', 'C029', 'S015'),
('O030', '15500', '2025-07-19', 'C030', 'S015');

--Quries
SELECT Customer.Name AS Customer_Name, Salesman.Name AS Salesman_Name, Salesman.City AS City_Name
FROM Customer
JOIN Salesman ON Customer.City = Salesman.City

--Linking Customer to their Salesman
SELECT Customer.Name AS Customer_Name, Salesman.Name AS Salesman_Name
FROM Customer
JOIN Salesman ON Customer.Salesman_ID = Salesman.Salesman_ID

--Fetching Order where Customer_City Dosen't match Salesman_City
SELECT Orders.Order_No, Customer.Name AS Customer_Name, Orders.Customer_ID, Orders.Salesman_ID, Customer.City AS Customer_City, Salesman.City AS Salesman_City
FROM Orders
JOIN Customer ON Orders.Customer_ID = Customer.Customer_ID
JOIN Salesman ON Orders.Salesman_ID = Salesman.Salesman_ID
WHERE Customer.City <> Salesman.City

--Fetching All Orders with Customer_Name
SELECT Orders.Order_No AS Order_Number, Customer.Name AS Customer_Name
FROM Orders
Join Customer ON Orders.Customer_ID = Customer.Customer_ID

--Customers with Salesman where comission is between 10-15
SELECT Customer.Name AS Customer_Name, Customer.City AS Customer_City, Salesman.Name AS Salesman_Name, Salesman.Commission AS Salesman_Comission
FROM Customer
JOIN Salesman ON Salesman.Salesman_ID = Customer.Salesman_ID
WHERE Salesman.Commission BETWEEN 10 AND 20

--
SELECT Orders.Order_No, Customer.Name AS Customer_Name, Salesman.Commission AS 'Commission Percentage', Orders.Purchase_Amount * Salesman.Commission AS 'Actual Amount'
FROM Orders
JOIN Salesman ON Orders.Salesman_ID = Salesman.Salesman_ID
JOIN Customer ON Orders.Customer_ID = Customer.Customer_ID
