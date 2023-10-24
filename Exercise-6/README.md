# Exercise 6 - Ingestion and Aggregation with PySpark

Here on our sixth exercise we will step it up a notch and start to use some
more common Big Data tools, in this case Spark and PySpark.

## Table of Content

- [Problem Statement](#problems-statement)
- [Project Workflow](#project-workflow)
- [Solution](#solution)

## Problems Statement

There is a folder called `data` in this current directory, `Exercises/Exercise-6`. Inside this folder there are two `zip`'d `csv` files, they should remain zipped for the duration of this exercise.

## Project Workflow

Generally the files look like this:

> trip_id,start_time,end_time,bikeid,tripduration,from_station_id,from_station_name,to_station_id,to_station_name,usertype,gender,birthyear
25223640,2019-10-01 00:01:39,2019-10-01 00:17:20,2215,940.0,20,Sheffield Ave & Kingsbury St,309,Leavitt St & Armitage Ave,Subscriber,Male,1987
25223641,2019-10-01 00:02:16,2019-10-01 00:06:34,6328,258.0,19,Throop (Loomis) St & Taylor St,241,Morgan St & Polk St,Subscriber,Male,1998

Your job is to read this files with `PySpark` and answer the following questions. Each question
should be output as a report in `.csv` format in a `reports` folder.

1. What is the `average` trip duration per day?
2. How many trips were taken each day?
3. What was the most popular starting trip station for each month?
4. What were the top 3 trip stations each day for the last two weeks?
5. Do `Male`s or `Female`s take longer trips on average?
6. What is the top 10 ages of those that take the longest trips, and shortest?

Note: Your `PySpark` code should be encapsulated inside functions or methods.

Extra Credit: Unit test your PySpark code.

## Solution

Coming Soon.
