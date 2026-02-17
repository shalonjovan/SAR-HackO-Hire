-- Create user (if not exists)
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles WHERE rolname = 'sar_user'
   ) THEN
      CREATE ROLE sar_user LOGIN PASSWORD 'sar_pass';
   END IF;
END
$$;

-- Create database (if not exists)
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'sar_prototype'
   ) THEN
      CREATE DATABASE sar_prototype OWNER sar_user;
   END IF;
END
$$;

-- Connect to database
\c sar_prototype

-- Grant privileges
GRANT ALL ON SCHEMA public TO sar_user;
ALTER SCHEMA public OWNER TO sar_user;

-- Create tables
CREATE TABLE IF NOT EXISTS accounts (
    account_id VARCHAR PRIMARY KEY,
    balance NUMERIC,
    status VARCHAR,
    account_type VARCHAR,
    opened_date DATE
);

CREATE TABLE IF NOT EXISTS kyc (
    customer_id VARCHAR PRIMARY KEY,
    full_name VARCHAR,
    risk_level VARCHAR,
    country VARCHAR,
    occupation VARCHAR
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id VARCHAR REFERENCES accounts(account_id),
    amount NUMERIC,
    type VARCHAR,
    timestamp TIMESTAMP
);

-- Insert sample data
INSERT INTO accounts VALUES
('ACC1001', 250000, 'ACTIVE', 'SAVINGS', '2021-06-15')
ON CONFLICT DO NOTHING;

INSERT INTO kyc VALUES
('CUST1001', 'John Doe', 'MEDIUM', 'India', 'Business Owner')
ON CONFLICT DO NOTHING;

INSERT INTO transactions (account_id, amount, type, timestamp)
VALUES
('ACC1001', 5000000, 'CREDIT', NOW()),
('ACC1001', 4500000, 'DEBIT', NOW()),
('ACC1001', 300000, 'CREDIT', NOW());
