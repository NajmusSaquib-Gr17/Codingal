CREATE TABLE IF NOT EXISTS PRODUCTS(
    PRODUCT_ID TEXT,
    PRODUCT_NAME TEXT,
    SELLER_ID TEXT,
    CATEGORY_ID TEXT,
    UNIT TEXT,
    PRICE REAL
);

INSERT INTO STUDENTS (PRODUCT_ID, PRODUCT_NAME, SELLER_ID, CATEGORY_ID, UNIT, PRICE)VALUES
('P001', 'ACI Salt 1kg', 50, 5),
('P002', 'PRAN Mango Juice 1L', 120, 10),
('P003', 'Fresh Soybean Oil 5L', 750, 20),
('P004', 'Bashundhara Tissue', 30, 3),
('P005', 'Molla Super Rice 25kg', 1600, 50),
('P006', 'Teer Flour 2kg', 110, 8),
('P007', 'Square Toiletries Soap', 45, 4),
('P008', 'PRAN Tomato Sauce 500ml', 90, 7),
('P009', 'ACI Pure Spices (Chili) 200g', 80, 6),
('P010', 'Radhuni Masala Pack', 60, 5);
