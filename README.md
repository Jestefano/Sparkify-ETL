# Schema for Song Play Analysis
## General overview
This project contains code needed to create a database for Sparkify, this database will be used for analytical purposes.

## Purpose
Sparkify, a startup in the music streaming industry, wants to analyze data about songs and user activity.
To do so, right now they have JSON files to do the analysis, this JSON files are not of easy access to analyze data.
For this reason, they need a database that can fill their analytical goals.
They plan to use this database to understand the songs that their users are listening to.

## Database design and ETL pipeline
The database is constructed on PostgreSQL, and it follows a star schema for analytic focus.
The fact table is the songplays table. 
The dimension tables are users table, songs table, artists table and time.
In order to see the details about this step see create_tables.py and sql_queries.py

The ETL pipeline is the following:
- We extract data from JSON format into Python
- In Python we take the data into the right format.
- Finally, we load it into our PostgreSQL database called sparkifydb.
To see the details about this step see etl.py.

In order to run the whole ETL pipeline, first run create_tables.py and then run etl.py.

## Example
We provide example queries and results for song play analysis. 
If you want to test this queries yourself you can use _test.ipynb .

- An important query to keep track of is the number of free and paid users, and we can segment this using gender.

```sql
SELECT s.level, u.gender, count(*) quantity 
FROM songplays s 
JOIN users u 
ON u.user_id = s.user_id
GROUP BY s.level, u.gender
```

With the data that we have we can see that there are more females in the paid group than any other group.

- We can also check data quality with SQL queries:
```sql
SELECT 
    SUM(CASE WHEN year = 0 THEN 1 ELSE 0 END) year_quantity_null, 
    ROUND(AVG(CASE WHEN year = 0 THEN 1 ELSE 0 END)*100,2) year_percentage_null 
FROM songs
```

From this we can see that 43 songs do not have year provided.
And this represents roughly 60% of the total songs. 
This must be fixed since some analysis can be missinterpred.

## BI
I have built a Power BI dashboard that can be found [here](https://app.powerbi.com/view?r=eyJrIjoiNGQ5NTc5ZWYtYTljYi00MDY2LThlMTktYjE0Yzk5YmFkZDBiIiwidCI6ImNjNjNkZjFhLTZiYzktNGQ3My1iNzM0LWEyOTRkMzI1MzE4NyIsImMiOjR9).
We can use it to extract is extract insights such as:
- Women consume more the product than men. 
- The most used hour is 4pm

## Next steps
As any project, there are things that can be improved or added. 
Here I present a list of things that I consider are important for a second stage of the project.

- A data cleaning process to make sure the whole database has a high quality standard of data. 
As an example, currently, I presented a simple example of quality of data, but this example can be extended to check quality as a whole. 
- By now we have only extracted information from json format. 
For this reason we still need to extract information via Json to then upload into our PostgreSQL database. 
This is inefficient since the json step can be ommited. 

