"""
Retail Sales Forecasting and Customer Analytics
04 - Database Validation

This script validates key results from the SQLite database
against the results obtained during the Python data preparation stage.
"""

import sqlite3
from pathlib import Path

# Locate the database
project_path = Path(__file__).resolve().parent.parent
database_path = project_path / "03_SQL" / "retail_analytics.db"

# Connect to database
conn = sqlite3.connect(database_path)

# Validate delivered sales
query = """
SELECT
    COUNT(DISTINCT o.order_id) AS delivered_orders,
    COUNT(*) AS delivered_order_items,
    ROUND(SUM(oi.price), 2) AS total_product_sales
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered';
"""

result = conn.execute(query).fetchone()

print("Delivered orders:", result[0])
print("Delivered order items:", result[1])
print("Total product sales:", result[2])

# Monthly delivered sales analysis
monthly_sales_query = """
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
"""

monthly_results = conn.execute(monthly_sales_query).fetchall()

print("\nMonthly Delivered Sales:")
print("Month | Orders | Items | Product Sales | Freight | Avg Item Price")

for row in monthly_results:
    print(row)

# Product category performance analysis
category_query = """
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
"""

category_results = conn.execute(category_query).fetchall()

print("\nTop 10 Product Categories by Sales:")
print("Category | Items | Orders | Product Sales | Avg Item Price")

for row in category_results[:10]:
    print(row)

# Customer purchasing behaviour analysis
customer_query = """
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
"""

customer_results = conn.execute(customer_query).fetchall()

print("\nTop 10 Customers by Total Spend:")
print("Customer | Orders | Items | Total Spend | Avg Item Price | First Purchase | Last Purchase")

for row in customer_results[:10]:
    print(row)    

# Repeat customer behaviour analysis
repeat_customer_query = """
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
"""

repeat_result = conn.execute(repeat_customer_query).fetchone()

print("\nRepeat Customer Behaviour:")
print("Total customers:", repeat_result[0])
print("One-time customers:", repeat_result[1])
print("Repeat customers:", repeat_result[2])
print("Repeat customer percentage:", repeat_result[3], "%")
print("Maximum orders per customer:", repeat_result[4])

conn.close()