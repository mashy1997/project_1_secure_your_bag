DROP TABLE customer_transactions;
DROP TABLE merchants;
DROP TABLE categories;

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE merchants (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE customer_transactions (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  amount INT,
  merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
  category_id INT REFERENCES categories(id) ON DELETE CASCADE
);