CREATE DATABASE covid_analysis;
USE covid_analysis;

-- 1 table create 
CREATE TABLE covid_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100),
    report_date DATE,
    confirmed_cases INT,
    deaths INT,
    recovered INT
);

-- 2 sample data insert (Realistic)
INSERT INTO covid_data (country, report_date, confirmed_cases, deaths, recovered) VALUES
('India', '2020-04-01', 2000, 50, 150),
('India', '2020-05-01', 35000, 1200, 12000),
('India', '2020-06-01', 200000, 6000, 120000),

('USA', '2020-04-01', 300000, 8000, 15000),
('USA', '2020-05-01', 1200000, 70000, 200000),
('USA', '2020-06-01', 2500000, 130000, 800000),

('Brazil', '2020-04-01', 10000, 500, 2000),
('Brazil', '2020-05-01', 500000, 30000, 200000),
('Brazil', '2020-06-01', 1200000, 60000, 700000);

-- 3. tatal cases & death country_wise
SELECT
    country,
    SUM(confirmed_cases) AS total_cases,
    SUM(deaths) AS total_deaths
FROM covid_data
GROUP BY country
ORDER BY total_cases DESC;

-- 4. monthly wise global casese(trend)
SELECT 
    DATE_FORMAT(report_date, '%Y-%m') AS month,
    SUM(confirmed_cases) AS total_cases
FROM covid_data
GROUP BY month 
ORDER BY month;

-- 5. death rate % by contry 
SELECT
    country,
    ROUND(SUM(deaths) / SUM(confirmed_cases) * 100, 2) AS death_rate_percent
FROM covid_data
GROUP BY country
ORDER BY death_rate_percent DESC;

-- 6. TOP 3 worst affected 
SELECT 
    country, 
    SUM(confirmed_cases) AS total_cases
FROM covid_data
GROUP BY country
ORDER BY total_cases DESC
LIMIT 3;

-- 7. recovey rate analysis 
SELECT
    country,
    ROUND(SUM(recovered) / SUM(confirmed_cases) * 100, 2) AS recovery_rate_percent
FROM covid_data
GROUP BY country
ORDER BY recovery_rate_percent DESC;

