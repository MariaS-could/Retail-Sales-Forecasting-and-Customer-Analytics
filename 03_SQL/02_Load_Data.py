"""
Retail Sales Forecasting and Customer Analytics
02 - Load Data into SQLite

This script loads the prepared and validated Olist datasets into
the SQLite relational database.

Cleaned datasets are used where transformation was required.
Sellers and order items are loaded from the original source files
because data-quality checks showed that no additional transformation
was required for the fields used in the relational database.
"""

import sqlite3
import pandas as pd
from pathlib import Path

# Project paths
project_path = Path(__file__).resolve().parent.parent
cleaned_data_path = project_path / "02_Cleaned_Data"
raw_data_path = project_path / "01_Raw_Data"
database_path = project_path / "03_SQL" / "retail_analytics.db"

# Connect to SQLite database
conn = sqlite3.connect(database_path)
conn.execute("PRAGMA foreign_keys = ON;")

print("Database connection successful.")


# --------------------------------------------------
# Load source datasets
# --------------------------------------------------

customers = pd.read_csv(
    cleaned_data_path / "customers_clean.csv"
)

products = pd.read_csv(
    cleaned_data_path / "products_clean.csv"
)

orders = pd.read_csv(
    cleaned_data_path / "orders_clean.csv"
)

geolocation = pd.read_csv(
    cleaned_data_path / "geolocation_postcode_clean.csv"
)

payments = pd.read_csv(
    cleaned_data_path / "payments_by_order_clean.csv"
)

sellers = pd.read_csv(
    raw_data_path / "olist_sellers_dataset.csv"
)

order_items = pd.read_csv(
    raw_data_path / "olist_order_items_dataset.csv"
)


# Convert pandas missing values to SQLite NULL values
orders = orders.astype(object).where(pd.notnull(orders), None)


# --------------------------------------------------
# Clear existing records
# --------------------------------------------------
# Child tables are cleared before parent tables to
# preserve foreign-key integrity.

conn.execute("DELETE FROM order_items;")
conn.execute("DELETE FROM payments_by_order;")
conn.execute("DELETE FROM orders;")
conn.execute("DELETE FROM sellers;")
conn.execute("DELETE FROM products;")
conn.execute("DELETE FROM customers;")
conn.execute("DELETE FROM geolocation;")

conn.commit()

print("Existing database records cleared.")


# --------------------------------------------------
# Load tables in foreign-key-safe order
# --------------------------------------------------

customers.to_sql(
    "customers",
    conn,
    if_exists="append",
    index=False
)
print("Customers loaded:", len(customers))

products.to_sql(
    "products",
    conn,
    if_exists="append",
    index=False
)
print("Products loaded:", len(products))

sellers.to_sql(
    "sellers",
    conn,
    if_exists="append",
    index=False
)
print("Sellers loaded:", len(sellers))

orders.to_sql(
    "orders",
    conn,
    if_exists="append",
    index=False
)
print("Orders loaded:", len(orders))

geolocation.to_sql(
    "geolocation",
    conn,
    if_exists="append",
    index=False
)
print("Geolocation rows loaded:", len(geolocation))

payments.to_sql(
    "payments_by_order",
    conn,
    if_exists="append",
    index=False
)
print("Payments loaded:", len(payments))

order_items.to_sql(
    "order_items",
    conn,
    if_exists="append",
    index=False
)
print("Order Items loaded:", len(order_items))


# --------------------------------------------------
# Final validation
# --------------------------------------------------

foreign_key_violations = conn.execute(
    "PRAGMA foreign_key_check;"
).fetchall()

print("\nForeign key violations:", len(foreign_key_violations))

if foreign_key_violations:
    print(foreign_key_violations)
else:
    print("No foreign key violations found.")

conn.close()

print("\nDatabase loading completed successfully.")
print("Database connection closed successfully.")