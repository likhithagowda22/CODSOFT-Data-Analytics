import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# -----------------------------
# 1. Bar Chart
# -----------------------------
plt.figure(figsize=(6,4))
df["Department"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# -----------------------------
# 2. Pie Chart
# -----------------------------
plt.figure(figsize=(6,6))
df["Department"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Department Distribution")
plt.ylabel("")
plt.show()

# -----------------------------
# 3. Line Chart
# -----------------------------
plt.figure(figsize=(7,4))
plt.plot(df["EmployeeID"], df["Salary"], marker="o")
plt.title("Employee Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# -----------------------------
# 4. Scatter Plot
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# -----------------------------
# 5. Histogram
# -----------------------------
plt.figure(figsize=(6,4))
plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

print("Task 3 Completed Successfully!")