import pandas as pd

# Load the dataset
df = pd.read_csv('Dataset .csv')

# Check the shape of the dataset
print(f"Number of Rows: {df.shape[0]}")
print(f"Number of Columns: {df.shape[1]}")

# Check for missing values in each column
missing_values = df.isnull().sum()
print("Missing Values in Each Column:\n", missing_values)

# Drop rows with any missing values
df_cleaned_rows = df.dropna()

# Drop columns with missing values
df_cleaned_columns = df.dropna(axis=1)

# Verify that there are no missing values in the cleaned data
print("Missing values after dropping rows:")
print(df_cleaned_rows.isnull().sum())
print("Missing values after dropping columns:")
print(df_cleaned_columns.isnull().sum())

# Check the new shapes after cleaning
print(f"New number of rows: {df_cleaned_rows.shape[0]}")
print(f"New number of columns: {df_cleaned_columns.shape[1]}")
# Check the data types of the columns
print(df.dtypes)

# Convert data types if necessary
# Example: Converting a column to 'int' or 'float'
df['column_name'] = df['column_name'].astype(int)

# Example: Converting a column to 'datetime'
df['date_column'] = pd.to_datetime(df['date_column'])
