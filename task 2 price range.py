import pandas as pd

# Load the dataset
df = pd.read_csv('Dataset.csv')

# Find the most common price range
most_common_price_range = df['Price range'].value_counts().idxmax()
print(f"The most common price range is: {most_common_price_range}")
# Calculate average rating for each price range
avg_rating_by_price = df.groupby('Price range')['Aggregate rating'].mean()
print("Average Rating for Each Price Range:\n", avg_rating_by_price)

# Group by 'Color' and 'Price range', and calculate the mean of 'Aggregate rating'
avg_rating_by_color_price = df.groupby(['Color', 'Price range'])['Aggregate rating'].mean().reset_index()

# Find the row with the highest average rating
highest_avg_rating_row = avg_rating_by_color_price.loc[avg_rating_by_color_price['Aggregate rating'].idxmax()]

# Extract the color and price range with the highest rating
highest_color = highest_avg_rating_row['Color']
highest_price_range = highest_avg_rating_row['Price range']
highest_rating = highest_avg_rating_row['Aggregate rating']

print(f"The color representing the highest average rating is: {highest_color}")
print(f"The price range is: {highest_price_range}")
print(f"The highest average rating is: {highest_rating}")


