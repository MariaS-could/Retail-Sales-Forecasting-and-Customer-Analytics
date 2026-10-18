/*
Retail Sales Forecasting and Customer Analytics
05 - SQL Analysis Queries

Purpose:
This script uses the relational database to produce business-focused
retail insights. Queries combine multiple tables and support the later
exploratory analysis and Power BI dashboard.
*/

-- 1. Monthly delivered sales performance

SELECT
    strftime('%Y-%m', o.order_purchase_timestamp) AS sales_month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(*) AS items_sold,
    ROUND(SUM(oi.price), 2) AS product_sales,
    ROUND(SUM(oi.freight_value), 2) AS freight_value,
    ROUND(AVG(oi.price), 2) AS average_item_price
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY sales_month
ORDER BY sales_month;

-- 2. Product category performance

SELECT
    p.category_name_clean AS product_category,
    COUNT(*) AS items_sold,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    ROUND(SUM(oi.price), 2) AS product_sales,
    ROUND(AVG(oi.price), 2) AS average_item_price
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN products p
    ON oi.product_id = p.product_id
WHERE o.order_status = 'delivered'
GROUP BY p.category_name_clean
ORDER BY product_sales DESC;

-- 3. Customer purchasing behaviour

SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(*) AS items_purchased,
    ROUND(SUM(oi.price), 2) AS total_spend,
    ROUND(AVG(oi.price), 2) AS average_item_price,
    MIN(o.order_purchase_timestamp) AS first_purchase,
    MAX(o.order_purchase_timestamp) AS last_purchase
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_unique_id
ORDER BY total_spend DESC;-- 3. Customer purchasing behaviour

SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(*) AS items_purchased,
    ROUND(SUM(oi.price), 2) AS total_spend,
    ROUND(AVG(oi.price), 2) AS average_item_price,
    MIN(o.order_purchase_timestamp) AS first_purchase,
    MAX(o.order_purchase_timestamp) AS last_purchase
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_unique_id
ORDER BY total_spend DESC;

-- 4. Repeat customer behaviour

WITH customer_orders AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_unique_id
)

SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN total_orders = 1 THEN 1 ELSE 0 END) AS one_time_customers,
    SUM(CASE WHEN total_orders > 1 THEN 1 ELSE 0 END) AS repeat_customers,
    ROUND(
        100.0 * SUM(CASE WHEN total_orders > 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS repeat_customer_percentage,
    MAX(total_orders) AS maximum_orders_per_customer
FROM customer_orders;

