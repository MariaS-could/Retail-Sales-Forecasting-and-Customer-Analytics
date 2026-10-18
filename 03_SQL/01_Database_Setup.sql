/*
Retail Sales Forecasting and Customer Analytics
01 - Database Setup

Purpose:
This script creates the relational database structure used for the
retail analytics project. The prepared Olist datasets will be stored
in relational tables to support SQL querying, validation and later
business analysis.

The original raw datasets are preserved separately. This database
uses the prepared datasets created during the Python data cleaning
and preparation stage.
*/

PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    customer_unique_id TEXT NOT NULL,
    customer_zip_code_prefix INTEGER,
    customer_city TEXT,
    customer_state TEXT,
    customer_lat REAL,
    customer_lng REAL
);
-- Products table
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    product_category_name TEXT,
    product_name_lenght REAL,
    product_description_lenght REAL,
    product_photos_qty REAL,
    product_weight_g REAL,
    product_length_cm REAL,
    product_height_cm REAL,
    product_width_cm REAL,
    product_category_name_english TEXT,
    category_name_clean TEXT NOT NULL
);
-- Orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    order_status TEXT NOT NULL,
    order_purchase_timestamp TEXT NOT NULL,
    order_approved_at TEXT,
    order_delivered_carrier_date TEXT,
    order_delivered_customer_date TEXT,
    order_estimated_delivery_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
-- Prepared postcode geolocation table
CREATE TABLE IF NOT EXISTS geolocation (
    geolocation_zip_code_prefix INTEGER PRIMARY KEY,
    geolocation_lat REAL NOT NULL,
    geolocation_lng REAL NOT NULL
);
-- Aggregated payments table
CREATE TABLE IF NOT EXISTS payments_by_order (
    order_id TEXT PRIMARY KEY,
    total_payment_value REAL NOT NULL,
    payment_records INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Sellers table
CREATE TABLE IF NOT EXISTS sellers (
    seller_id TEXT PRIMARY KEY,
    seller_zip_code_prefix INTEGER,
    seller_city TEXT,
    seller_state TEXT
);

-- Order items table
CREATE TABLE IF NOT EXISTS order_items (
    order_id TEXT NOT NULL,
    order_item_id INTEGER NOT NULL,
    product_id TEXT NOT NULL,
    seller_id TEXT NOT NULL,
    shipping_limit_date TEXT,
    price REAL NOT NULL,
    freight_value REAL NOT NULL,

    PRIMARY KEY (order_id, order_item_id),

    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);
