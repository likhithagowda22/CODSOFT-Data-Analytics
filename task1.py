import pandas as pd

# 1. Load Dataset
df = pd.read_csv("data.csv")

# 2. Display First 5 Rows
print("First 5 Rows:")
print(df.head())

# 3. Dataset Information
print("\nDataset Information:")
print(df.info())

# 4. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Check Duplicate Records
print("\nDuplicate Records:", df.duplicated().sum())

# 6. Remove Duplicate Records
df = df.drop_duplicates()

# 7. Fill Missing Values
# Numeric columns -> Mean
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Categorical columns -> Mode
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# 8. Correct Data Types
print("\nData Types:")
print(df.dtypes)

# Example:
# df["Age"] = df["Age"].astype(int)

# 9. Save Cleaned Dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nDataset cleaned successfully!")
print("Cleaned file saved as cleaned_data.csv")