import psycopg2
import csv

def connect():
    try:
        conn = psycopg2.connect(database='sales', user='postgres', password='password')
        print('Connection Succesful')
    except psycopg2.Error as e:
        print(f'Error {e} occurred')
    return conn 

def execute_query(conn, query, values=None):
    cursor = conn.cursor()
    try:
        if values is not None:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        print('Query Ran Successfully!')
    except psycopg2.Error as e:
        print(f"The error '{e}' occurred")
    
    conn.commit()
    cursor.close()


conn = connect()

# Run SQL DDL script 
def schema_script():

    with open('script.sql', 'r') as f: 
        sql_script = f.read()

        execute_query(conn, sql_script)


def ingest_accounts():

    with open('./data/accounts.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            insert_query = """INSERT INTO accounts (customer_id, first_name, last_name, address_1, address_2, city, state, zipcode, join_date) VALUES (%s, %s, %s , %s, %s, %s, %s, %s, %s)"""

            execute_query(conn, insert_query, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8] ))
        
        print('succesfully inputed data..')



# Ingest CSV into products table
def ingest_products():
    with open('./data/products.csv', 'r') as file: 
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            insert_query = """INSERT INTO products (product_id, product_code, product_description) VALUES (%s, %s, %s)"""

            execute_query(conn, insert_query, (row[0], row[1], row[2]))
        
        print('succesfully inputed data..')



# Ingest CSV into transaction table
def ingest_transactions():

    with open('./data/transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            insert_query = """INSERT INTO transactions (transaction_id, transaction_date, product_id, quantity, customer_id) VALUES (%s, %s, %s , %s, %s)"""

            execute_query(conn, insert_query, (row[0], row[1], row[2], row[5], row[6]))
        
        print('succesfully inputed data..')




ingest_accounts()
ingest_products()
ingest_transactions()




conn.close()