import pandas as pd

# Load the data
df = pd.read_csv('online_retail.csv', encoding='latin1')
print("Original shape:", df.shape)

# Step 1: Remove duplicates
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

# Step 2: Remove rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])
print("After removing missing CustomerID:", df.shape)

# Step 3: Remove cancellations (InvoiceNo starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
print("After removing cancellations:", df.shape)

# Step 4: Remove negative or zero quantities and prices
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
print("After removing bad quantities/prices:", df.shape)

# Step 5: Fix the date column
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Step 6: Add a Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Save clean file
df.to_csv('online_retail_clean.csv', index=False)
print("\nDone! Clean file saved.")