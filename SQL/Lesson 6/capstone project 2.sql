-- 1. Create the Restaurants table
CREATE TABLE IF NOT EXISTS Restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    neighborhood TEXT,
    cuisine TEXT,
    price TEXT CHECK (price IN ('$', '$$', '$$$', '$$$$')),  -- $, $$, $$$, $$$$
    rating REAL,         -- 1.0 to 5.0
    health_grade TEXT CHECK (health_grade IN ('A', 'B', 'C') OR health_grade IS NULL)  -- A, B, C, or NULL
);

-- 2. Insert realistic Dhaka-based restaurant data
INSERT INTO Restaurants (id, name, neighborhood, cuisine, price, rating, health_grade) VALUES
(1, 'Star Kabab', 'Dhanmondi', 'Bangladeshi', '$', 4.2, 'A'),
(2, 'Sajna Restaurant', 'Gulshan', 'Indian', '$$', 4.3, 'A'),
(3, 'Sushi Samurai', 'Banani', 'Japanese', '$$$', 4.7, 'A'),
(4, 'Mainland China', 'Gulshan', 'Chinese', '$$', 4.5, 'A'),
(5, 'Pizza Roma', 'Dhanmondi', 'Italian', '$$', 3.9, 'B'),
(6, 'Cafe Candyman', 'Uttara', 'Dessert', '$$', 4.1, NULL),
(7, 'Boomers Cafe', 'Bashundhara', 'American', '$$', 3.7, NULL),
(8, 'Sultans Dine', 'Dhanmondi', 'Bangladeshi', '$$', 4.8, 'A'),
(9, 'Izumi', 'Gulshan', 'Japanese', '$$$$', 4.6, 'A'),
(10, 'Spicy Sichuan Express', 'Banani', 'Chinese', '$', 4.0, 'B'),
(11, 'Bella Italia', 'Gulshan', 'Italian', '$$$', 4.4, 'A'),
(12, 'Chopsticks', 'Uttara', 'Chinese', '$', 3.5, 'C');

-- 3. View full table
SELECT * FROM Restaurants;

-- 4. Distinct neighborhoods
SELECT DISTINCT neighborhood AS Distinct_Neighborhoods
FROM Restaurants;

-- 5. Distinct cuisine types
SELECT DISTINCT cuisine AS Distinct_Cuisine_Types
FROM Restaurants;

-- 6. Chinese takeout options
SELECT * FROM Restaurants
WHERE cuisine = 'Chinese';

-- 7. Restaurants with rating >= 4
SELECT * FROM Restaurants
WHERE rating >= 4;

-- 8. Italian restaurants with $$$ price (Abbi & Ilana)
SELECT * FROM Restaurants
WHERE cuisine = 'Italian' AND price = '$$$';

-- 9. Restaurants with 'Candy' in the name (Trey's memory)
SELECT * FROM Restaurants
WHERE name LIKE '%Candy%';

-- 10. Restaurants in Gulshan, Dhanmondi, or Banani
SELECT * FROM Restaurants
WHERE neighborhood IN ('Gulshan', 'Dhanmondi', 'Banani');

-- 11. Health grade pending restaurants
SELECT * FROM Restaurants
WHERE health_grade IS NULL;

-- 12. Top 4 restaurants by rating
SELECT * FROM Restaurants
ORDER BY rating DESC
LIMIT 4;
