# Exercise #5 - Data Modeling for Postgres + Python.

In this fifth exercise you will work on a few different topics,
data modeling, Python, and Postgres. These are common problems worked 
on in data engineering.

## Table of Content

- [Problem Statement](#problems-statement)
- [Project Workflow](#project-workflow)
- [Solution](#solution)

## Problems Statement

There is a folder called `data` in this current directory, `Exercises/Exercise-5`. There are also
3 `csv` files located in that folder. Open each one and examine it, the  first task is to create a `sql` script with the `DDL` to hold a `CREATE` statement for each data file. Remember to think about data types. Also, this `CREATE` statements should include indexes for each table, as well as primary and foreign keys.

After you have finished this `sql` scripts, we must connect to `Postgres` using the `Python` package
called `psycopg2`. Once connected we will run our `sql` scripts against the database.

Finally, we will use `psycopg2` to insert the data in each `csv` file into the table you created.

## Project Workflow

Generally, your script should do the following:

1. Examine each `csv` file in `data` folder. Design a `CREATE` statement for each file.
2. Ensure you have indexes, primary and forgein keys.
3. Use `psycopg2` to connect to `Postgres` on `localhost` and the default `port`.
4. Create the tables against the database.
5. Ingest the `csv` files into the tables you created, also using `psycopg2`

## Solution
