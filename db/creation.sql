CREATE TABLE IF NOT EXISTS customers (
    CustomerID int primary key,
    Genre varchar(10),
    Age int,
    Annual_Income int,
    Spending_Score int
);

CREATE TABLE IF NOT EXISTS ehnois (
    index int,
    name varchar,
    age int
);

COPY customers(CustomerID,Genre,Age,Annual_Income,Spending_Score)
FROM '/data/Mall_Customers.csv'
DELIMITER ','
CSV HEADER;
