-- 1. Create and select the database
CREATE DATABASE IF NOT EXISTS customer_churn_db;
USE customer_churn_db;

-- 2. Create the core 'customers' table
CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    tenure_months INT NOT NULL,
    monthly_charges DECIMAL(10, 2) NOT NULL,
    account_status VARCHAR(20) NOT NULL,
    churned INT NOT NULL
);

-- 3. Create the 'usage_stats' table
CREATE TABLE usage_stats (
    customer_id VARCHAR(20) NOT NULL,
    total_support_tickets INT NOT NULL,
    days_since_last_login INT NOT NULL,
    -- Establishes the link between both tables
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);