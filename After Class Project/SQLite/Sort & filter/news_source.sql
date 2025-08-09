CREATE TABLE hacker_news (
    NewsID INT PRIMARY KEY,
    Title VARCHAR(255),
    Category VARCHAR(50),
    Author VARCHAR(50),
    Score INT
);


INSERT INTO hacker_news (NewsID, Title, Category, Author, Score)
VALUES
(1, 'AI Breakthrough in 2025', 'Technology', 'Alice', 95),
(2, 'Stock Market Crash Predictions', 'Finance', 'Bob', 88),
(3, '10 Tips for Remote Work', 'Lifestyle', 'Charlie', 72),
(4, 'Quantum Computing Milestone', 'Technology', 'David', 99),
(5, 'Best Programming Languages', 'Technology', 'Eve', 89),
(6, 'Global Climate Report', 'Environment', 'Frank', 93),
(7, 'Startup Raises $100M', 'Business', 'Grace', 85),
(8, 'SpaceX Mars Mission Update', 'Technology', 'Henry', 97);


SELECT Category, AVG(Score) AS AvgScore
FROM hacker_news
GROUP BY Category;

SELECT Category, AVG(Score) AS AvgScore
FROM hacker_news
GROUP BY Category
HAVING AVG(Score) > 90;

SELECT * FROM hacker_news
ORDER BY Score DESC;

SELECT * FROM hacker_news
WHERE Category = 'Technology' AND Score > 90
ORDER BY Score DESC;
