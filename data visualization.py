import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Dataset.csv')

# Remove missing ratings
df = df.dropna(subset=['Aggregate rating'])

# 1. Distribution of Ratings (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(df['Aggregate rating'], bins=10, kde=True, color='blue')
plt.title('Distribution of Aggregate Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# 2. Distribution of Ratings (Bar Plot)
plt.figure(figsize=(10, 6))
sns.countplot(x='Aggregate rating', data=df, palette='viridis')
plt.title('Number of Restaurants per Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()
# Ensure 'Cuisines' column is clean
df['Cuisines'] = df['Cuisines'].apply(lambda x: [c.strip() for c in str(x).split(',')])
df_exploded = df.explode('Cuisines')

# Average Ratings per Cuisine
cuisine_avg_rating = df_exploded.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
cuisine_avg_rating = cuisine_avg_rating.sort_values(by='Aggregate rating', ascending=False)

# Top 10 cuisines by average rating
top_cuisines = cuisine_avg_rating.head(10)

# Plotting Average Ratings of Top 10 Cuisines
plt.figure(figsize=(12, 6))
sns.barplot(x='Aggregate rating', y='Cuisines', data=top_cuisines, palette='magma')
plt.title('Top 10 Cuisines with Highest Average Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Cuisine')
plt.show()
# Average Ratings per City
city_avg_rating = df.groupby('City')['Aggregate rating'].mean().reset_index()
city_avg_rating = city_avg_rating.sort_values(by='Aggregate rating', ascending=False)

# Top 10 cities by average rating
top_cities = city_avg_rating.head(10)

# Plotting Average Ratings of Top 10 Cities
plt.figure(figsize=(12, 6))
sns.barplot(x='Aggregate rating', y='City', data=top_cities, palette='coolwarm')
plt.title('Top 10 Cities with Highest Average Ratings')
plt.xlabel('Average Rating')
plt.ylabel('City')
plt.show()
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Votes', y='Aggregate rating', data=df, color='green')
plt.title('Votes vs. Rating')
plt.xlabel('Number of Votes')
plt.ylabel('Rating')
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(x='Price range', y='Aggregate rating', data=df, palette='Set2')
plt.title('Ratings Across Different Price Ranges')
plt.xlabel('Price Range')
plt.ylabel('Rating')
plt.show()
# Assuming 'Has Online Delivery' column is encoded with 1 for 'Yes' and 0 for 'No'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Has Online delivery', y='Aggregate rating', data=df, palette='Set1')
plt.title('Impact of Online Delivery on Ratings')
plt.xlabel('Has Online Delivery (1 = Yes, 0 = No)')
plt.ylabel('Rating')
plt.show()

