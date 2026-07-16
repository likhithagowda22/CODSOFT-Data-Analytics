import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Mean
print("\nMean:")
print(df.mean(numeric_only=True))

# Median
print("\nMedian:")
print(df.median(numeric_only=True))

# Mode
print("\nMode:")
print(df.mode())

# Correlation
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# Histogram
df.hist(figsize=(10,6))
plt.show()

# Box Plot
df.boxplot(figsize=(10,6))
plt.show()

# Bar Chart
df["Department"].value_counts().plot(kind="bar")
plt.title("Employees in Each Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

print("\nEDA Completed Successfully!")