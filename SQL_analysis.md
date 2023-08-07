## Analysis using SQL

#### Task 1: Give the count of the minimum number of days for the time when temperature reduced

<pre>
WITH T1 AS
(SELECT DATE, TEMPERATURE,
ROW_NUMBER() OVER (ORDER BY DATE) AS ROW_ID,
LEAD(TEMPERATURE) OVER (ORDER BY DATE) AS LEAD_DATE
FROM weatherdata), 
T2 AS
(SELECT ROW_ID, DATE, TEMPERATURE, LEAD_DATE,
ROW_NUMBER() OVER (ORDER BY DATE) AS ROW_NUM,
ROW_ID - ROW_NUMBER() OVER (ORDER BY DATE) AS DIFF
FROM T1
WHERE TEMPERATURE > LEAD_DATE), 
T3 AS
(SELECT *, COUNT(*) OVER (PARTITION BY DIFF) AS CONC_DAYS 
FROM T2)
SELECT MIN(CONC_DAYS) FROM T3;
</pre>

#### Task 2: Find the temperature as Cold / hot by using the case and avg of values of the given data set

<pre>
SELECT
    DATE, AVG(TEMPERATURE),
    CASE 
        WHEN AVG(TEMPERATURE) > 50 THEN 'HOT'
        ELSE 'COLD'
    END AS TEMPERATURE
FROM weatherdata
GROUP BY DATE;
</pre>

#### Task 3: Can you check for all 4 consecutive days when the temperature was below 30 Fahrenheit

<pre>
WITH T1 AS
(SELECT *,
ROW_NUMBER() OVER (ORDER BY DATE) AS ROW_ID
FROM weatherdata), T2 AS
(SELECT DATE, TEMPERATURE, ROW_ID,
ROW_NUMBER() OVER (ORDER BY DATE) AS ROW_NUM,
ROW_ID - ROW_NUMBER() OVER (ORDER BY DATE) AS DIFF
FROM T1
WHERE TEMPERATURE < 30), T3 AS
(SELECT *, COUNT(*) OVER (partition by DIFF) AS CONC_DAYS FROM T2)
SELECT DATE, TEMPERATURE FROM T3 WHERE CONC_DAYS = 4;
</pre>

#### Task 4: Can you find the maximum number of days for which temperature dropped

<pre>
WITH T1 AS
(SELECT DATE, TEMPERATURE,
ROW_NUMBER() OVER (ORDER BY DATE) AS ROW_ID,
LEAD(TEMPERATURE) OVER (ORDER BY DATE) AS LEAD_DATE
FROM weatherdata), 
T2 AS
(SELECT ROW_ID, DATE, TEMPERATURE, LEAD_DATE,
ROW_NUMBER() OVER (ORDER BY DATE) AS ROW_NUM,
ROW_ID - ROW_NUMBER() OVER (ORDER BY DATE) AS DIFF
FROM T1
WHERE TEMPERATURE > LEAD_DATE), 
T3 AS
(SELECT *, COUNT(*) OVER (PARTITION BY DIFF) AS CONC_DAYS 
FROM T2)
SELECT MAX(CONC_DAYS) FROM T3;
</pre>

#### Task 5: Can you find the average of average humidity from the dataset 

<pre>
SELECT DATE, AVG(AVG_HUMIDITY_PERC) as AVG_HUMIDITY
FROM weatherdata
GROUP BY DATE
ORDER BY DATE;
</pre>

#### Task 6: Use the GROUP BY clause on the Date column and make a query to fetch details for average windspeed ( which is now windspeed done in task 3 )

<pre>
SELECT DATE, AVG(AVG_WINDSPEED_MPH) AS AVG_WINDSPEED
FROM weatherdata
GROUP BY DATE
ORDER BY DATE;
</pre>

#### Task 7: Please add the data in the dataset for 2034 and 2035 as well as forecast predictions for these years 

<pre>
LOAD DATA INFILE 'cleaned_weather_dataset_with_forecast.csv'
IGNORE INTO TABLE weatherdata
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
</pre>

#### Task 8: If the maximum gust speed increases from 55mph, fetch the details for the next 4 days

<pre>
SELECT wd.DATE, wd.MAX_GUSTSPEED_MPH
FROM weatherdata wd
INNER JOIN (SELECT DATE FROM weatherdata WHERE MAX_GUSTSPEED_MPH > 55) sub
ON wd.DATE BETWEEN sub.DATE AND DATE_ADD(sub.DATE, INTERVAL 4 DAY);
</pre>

#### Task 9: Find the number of days when the temperature went below 0 degrees Celsius 

<pre>
SELECT COUNT(*) FROM weatherdata
WHERE TEMPERATURE < 0;
</pre>

#### Task 10: Create another table with a “Foreign key” relation with the existing given data set.

<pre>
-- Created index on our weather analysis dataset. 
CREATE INDEX idx_date ON weatherdata (DATE);
-- Created another table with a “Foreign Key” 
CREATE TABLE incharge_details(
	ID INT NOT NULL PRIMARY KEY,
    	INCHARGE_NAME VARCHAR(50),
    	DEPARTMENT VARCHAR(50),
    	ENTRY_DATE DATE,
   	FOREIGN KEY(ENTRY_DATE) REFERENCES weatherdata(DATE)
);
</pre>