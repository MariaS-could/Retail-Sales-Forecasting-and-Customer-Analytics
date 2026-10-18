/*
Retail Sales Forecasting and Customer Analytics
03 - Database Validation Queries

Purpose:
This script validates the relational database after data loading.
The checks confirm that the expected number of records were loaded
into each table before further SQL analysis is performed.
*/

-- Check number of records in each table

SELECT 'customers' AS table_name, COUNT(*) AS row_count
FROM customers

UNION ALL

SELECT 'products', COUNT(*)
FROM products

UNION ALL

SELECT 'sellers', COUNT(*)
FROM sellers

UNION ALL

SELECT 'orders', COUNT(*)
FROM orders

UNION ALL

SELECT 'geolocation', COUNT(*)
FROM geolocation

UNION ALL

SELECT 'payments_by_order', COUNT(*)
FROM payments_by_order

UNION ALL

SELECT 'order_items', COUNT(*)
FROM order_items;

-- Check foreign key relationships
PRAGMA foreign_key_check;

-- Validate delivered sales against Python cleaning results

SELECT
    COUNT(DISTINCT o.order_id) AS delivered_orders,
    COUNT(*) AS delivered_order_items,
    ROUND(SUM(oi.price), 2) AS total_product_sales
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered';

