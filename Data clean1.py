import numpy as np
import pandas as pd


# Load the dataset
df = pd.read_csv("data/indian_employee_data.csv")

print(df.head())


# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())


# Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)


# Remove duplicate records
df.drop_duplicates(inplace=True)


# Replace negative salary values with the mean salary
salary_mean = df.loc[
    df["Salary (INR)"] >= 0,
    "Salary (INR)"
].mean()

df["Salary (INR)"] = np.where(
    df["Salary (INR)"] < 0,
    salary_mean,
    df["Salary (INR)"]
)


# Handle missing salary values
df["Salary (INR)"].fillna(
    df["Salary (INR)"].mean(),
    inplace=True
)


# Handle missing performance ratings
df["Performance Rating"].fillna(
    df["Performance Rating"].median(),
    inplace=True
)


# Fill remaining numerical missing values
df.fillna(
    df.mean(numeric_only=True),
    inplace=True
)


# Detect salary outliers using the 3-Sigma rule
salary_mean = df["Salary (INR)"].mean()
salary_std = df["Salary (INR)"].std()

lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[
    (df["Salary (INR)"] >= lower_bound) &
    (df["Salary (INR)"] <= upper_bound)
]


# Final data quality check
print("\nData after cleaning:")
print(df.head())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print(
    "Negative salary values:",
    (df["Salary (INR)"] < 0).sum()
)


# Save cleaned dataset
df.to_csv(
    "data/cleaned_indian_employee_data.csv",
    index=False
)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved successfully.")