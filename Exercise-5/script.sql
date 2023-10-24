
drop table  IF exists accounts CASCADE;

CREATE TABLE accounts(
	customer_id int NOT NULL,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	address_1 varchar(100)  NOT NULL,
	address_2 varchar(100),
	city varchar(30) NOT NULL,
	state varchar(30) NOT NULL,
	zipcode int NOT NULL,
	join_date date NOT NULL,
	PRIMARY KEY (customer_id)
);

CREATE INDEX account_idx on accounts (join_date, city, join_date);

DROP table if exists products CASCADE;

CREATE TABLE products(
	product_id int,
	product_code int,
	product_description varchar(100),
	PRIMARY KEY(product_id)
);

DROP table if exists transactions CASCADE;

CREATE TABLE transactions(
	transaction_id varchar(100),
	transaction_date date,
	product_id int,
	quantity int,
	customer_id int, 
	PRIMARY KEY(transaction_id),
	FOREIGN KEY(product_id) REFERENCES products(product_id),
	FOREIGN KEY(customer_id) REFERENCES accounts(customer_id)
);

CREATE INDEX transactions_idx  on transactions(transaction_date);

-- SELECT indexname FROM pg_indexes WHERE tablename = 'transactions';
