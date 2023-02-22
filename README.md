# Weather Forecasting Analysis and Visualization

## About the project:
Weather prediction is one of the most certainly required information in all over the regions
It involves collecting global meteorological surface and upper-air observations, preparing global surface and upper air pressure, temperature, moisture, and wind analyses at frequent time intervals based upon these observations we predict some data for upcoming days weather conditions

## Project Description: 

This data contains day wise weather attributes from 2022 to July 2033 (predicted data)
Columns are as follows :
Date
Average temperature (°F)
Average humidity (%)
Average dewpoint (°F)
Average barometer (in)
Average windspeed (mph)
Average gust speed (mph)
Average direction (°degree)
Rainfall for month (in)
Rainfall for year (in)
Maximum rain per minute
Maximum temperature (°F)
Minimum temperature (°F)
Maximum humidity (%)
Minimum humidity (%)
Maximum pressure
Minimum pressure
Maximum wind speed (mph)
Maximum gust speed (mph)
Maximum heat index (°F)


NOTE: the given data requires cleaning and analysis to proceed further for any analysis.

The Project will consist of 2 modules:
Module 1: Pre-processing, Analysing data using Python and SQL.
Module 2: Visualizing data using Power bi.

Prerequisites for the Project (mandatory): 
1.	SQL (MYSQL)
2.	POWER BI/ Tableau
3.	Excel
4.	Python


## Module 1: Pre-processing, Analysing data using SQL

In this module, you will query the dataset using structured query language to gain insights from the database. The problem statements to be solved will be provided to you and you need to provide the solution for the same using your logic. Different concepts of SQL will be used in this process such as aggregating the data, grouping the data, ordering the data, etc. Module 1 consists of subtasks which are as follows

➢	Task 1: Pre-processing the data

Data preprocessing is one of the important steps in data analytics because data that is not processed can lead to different unwanted results when the data is used for further applications. This task includes sub-tasks such as handling null values, deletion or transformation of irrelevant values, data type transformation, removing duplicates, etc. The tasks to be performed for cleaning the data set are given below:


*Here is the link to the data set for the module: Click here

●	Subtask 1: Correct years for given data set
        
●	Subtask 2: removal of duplicate rows and duplicate Columns

●	Subtask 3: fix a few labels in the given data set 

●	Subtask 4: Encoding data into suitable format


➢	Task 2: Go through both cleaned datasets for a perfect understanding:

Since you have analyzed the complete data set accurately, Let's answer the following requirements to proceed further for a better understanding 

1.	Give the count of the minimum number of days for the time when temperature reduced

2.	Find the temperature as Cold / hot by using the case and avg of values of the given data set

3.	Can you check for all 4 consecutive days when the temperature was below 30 Fahrenheit

4.	Can you find the maximum number of days for which temperature dropped

5.	Can you find the average of average humidity from the dataset (NOTE: should contain the following clauses: group by, order by, date)

6.	Use the GROUP BY clause on the Date column and make a query to fetch details for average windspeed (which is now windspeed done in task 3)

7.	Please add the data in the dataset for 2034 and 2035 as well as forecast predictions for these years (NOTE: data consistency and uniformity should be maintained)

8.	If the maximum gust speed increases from 55mph, fetch the details for the next 4 days

9.	Find the number of days when the temperature went below 0 degrees Celsius 

10.	 Create another table with a “Foreign key” relation with the existing given data set.



## Module 2: Visualizing data using Power BI

Here comes the next module. You will use the weather datasets and the data table you created to visualize what the numbers in and behind the data want to convey. You have to create a dashboard for the same using different statistical graphs and diagrams for a visual understanding and analysis. Given below are the requirements, create a dashboard consisting of mentioned visuals.


1.	Design a dashboard of your choice and imagination with attractive wallpapers and design visuals


2.	The dashboard must consist of basic power bi visuals like stacked bar charts, cards, line charts, pie charts, etc.


3.	You can use any visual capable of representing the given dataset.


4.	Columns having numeric data types are to be majorly used in visuals


5.	Include the Weather dataset and the data table you created in the above task ( question 10 ).

