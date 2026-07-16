import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_data.csv")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Descriptive Statistics
print("\nSummary Statistics:")
print(df.describe())

# Highest Spending Customer
highest = df.loc[df["Amount"].idxmax()]
print("\nHighest Spending Customer:")
print(highest)

# Average Purchase by City
city_avg = df.groupby("City")["Amount"].mean()
print("\nAverage Purchase by City:")
print(city_avg)

# Product Sales
product_sales = df.groupby("Product")["Amount"].sum()
print("\nProduct Sales:")
print(product_sales)

# ---------------- Bar Chart ----------------
plt.figure(figsize=(6,4))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# ---------------- Pie Chart ----------------
plt.figure(figsize=(6,6))
city_avg.plot(kind="pie", autopct="%1.1f%%")
plt.title("Average Purchase by City")
plt.ylabel("")
plt.show()

# ---------------- Scatter Plot ----------------
plt.figure(figsize=(6,4))
plt.scatter(df["Age"], df["Amount"])
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Amount")
plt.grid(True)
plt.show()

print("\nCustomer Data Analysis Completed Successfully!")