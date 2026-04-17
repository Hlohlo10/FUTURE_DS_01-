import pandas as pd
import matplotlib.pyplot as plt
import os

# Creates a folder to save all charts
os.makedirs('charts', exist_ok=True)

# Loading the clean data
df = pd.read_csv('online_retail_clean.csv', encoding='latin1')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

print("Data loaded successfully!")
print(f"Total Revenue: ${df['Revenue'].sum():,.2f}")
print(f"Total Orders: {df['InvoiceNo'].nunique():,}")
print(f"Total Customers: {df['CustomerID'].nunique():,}")
print(f"Total Products: {df['Description'].nunique():,}")

# ── CHART 1: Monthly Revenue Trend ──────────────────────────────
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Revenue'].sum()

plt.figure(figsize=(12, 5))
monthly_revenue.plot(kind='line', marker='o', color='steelblue', linewidth=2)
plt.title('Monthly Revenue Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Revenue (£)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/monthly_revenue.png')
plt.close()
print("Chart 1 saved: Monthly Revenue Trend")

# ── CHART 2: Top 10 Products by Revenue ─────────────────────────
top_products = (df.groupby('Description')['Revenue']
                .sum()
                .sort_values(ascending=False)
                .head(10))

plt.figure(figsize=(12, 6))
top_products.plot(kind='barh', color='steelblue')
plt.title('Top 10 Products by Revenue', fontsize=16, fontweight='bold')
plt.xlabel('Revenue (£)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('charts/top_products.png')
plt.close()
print("Chart 2 saved: Top 10 Products")

# ── CHART 3: Top 10 Countries by Revenue ────────────────────────
top_countries = (df.groupby('Country')['Revenue']
                 .sum()
                 .sort_values(ascending=False)
                 .head(10))

plt.figure(figsize=(12, 6))
top_countries.plot(kind='bar', color='coral')
plt.title('Top 10 Countries by Revenue', fontsize=16, fontweight='bold')
plt.xlabel('Country')
plt.ylabel('Revenue (£)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/top_countries.png')
plt.close()
print("Chart 3 saved: Top 10 Countries")

# ── CHART 4: Top 10 Customers by Revenue ────────────────────────
top_customers = (df.groupby('CustomerID')['Revenue']
                 .sum()
                 .sort_values(ascending=False)
                 .head(10))

plt.figure(figsize=(10, 5))
top_customers.plot(kind='bar', color='mediumseagreen')
plt.title('Top 10 Customers by Revenue', fontsize=16, fontweight='bold')
plt.xlabel('Customer ID')
plt.ylabel('Revenue (£)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/top_customers.png')
plt.close()
print("Chart 4 saved: Top 10 Customers")

print("\nAll charts saved in the 'charts' folder!")