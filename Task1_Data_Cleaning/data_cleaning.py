import pandas as pd

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATES")
print(df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize Gender
df["Gender"] = df["Gender"].str.strip()
df["Gender"] = df["Gender"].str.capitalize()

print("\nUNIQUE GENDER VALUES")
print(df["Gender"].unique())

# Rename columns
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATA TYPES")
print(df.dtypes)

print("\nSTATISTICS")
print(df.describe())

# Save cleaned dataset
df.to_csv("cleaned_mall_customers.csv", index=False)

print("\nSUCCESS!")
print("cleaned_mall_customers.csv created")
