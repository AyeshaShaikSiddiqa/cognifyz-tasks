import pandas as pd
df = pd.read_csv('Dataset.csv')
# Create a new feature representing the length of the restaurant name
df['Restaurant Name Length'] = df['Restaurant Name'].apply(len)

# Create a new feature representing the length of the address
df['Address Length'] = df['Address'].apply(len)

# Convert 'Has Table booking' and 'Has Online delivery' to binary values (1 for 'Yes', 0 for 'No')
df['Has Table Booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online Delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

# Display the first few rows of the updated dataset to verify
print(df[['Restaurant Name', 'Restaurant Name Length', 'Address', 'Address Length', 'Has Table Booking', 'Has Online Delivery']].head())

# Create a new feature representing the number of cuisines offered
df['Cuisine Count'] = df['Cuisines'].apply(lambda x: len(x.split(',')) if pd.notna(x) else 0)

# Ensure Price range is in numerical format (if not already)
df['Price range'] = df['Price range'].astype(int)
