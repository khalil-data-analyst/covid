import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\KHALIL\\Desktop\\covid.csv")

# Show basic info
print("First 5 rows:")
print(df.head())
print(df.tail())
print("\nColumn Names:")
print(df.columns)

print("\nNull values:")
print(df.isnull().sum())
