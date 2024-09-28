import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv('Dataset .csv')

city_distribution = df['City'].value_counts().head(10)  # Top 10 cities
print(city_distribution)


plt.figure(figsize=(10,6))
sns.barplot(x=city_distribution.values, y=city_distribution.index, palette='Set2')
plt.title('Top 10 Cities with Most Restaurants')
plt.xlabel('Number of Restaurants')
plt.ylabel('City')
plt.show()

# Similarly, analyze by country
country_distribution = df['Country Code'].value_counts().head(10)
print(country_distribution)

# Plot country distribution
plt.figure(figsize=(10,6))
sns.barplot(x=country_distribution.values, y=country_distribution.index, palette='Set2')
plt.title('Top 10 Countries with Most Restaurants')
plt.xlabel('Number of Restaurants')
plt.ylabel('Country')
plt.show()
# Scatter plot for rating vs location
plt.figure(figsize=(10,6))
sns.scatterplot(x='Longitude', y='Latitude', hue='Aggregate rating', data=df, palette='coolwarm')
plt.title('Restaurant Ratings by Location (Latitude & Longitude)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

average_rating_city = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
print(average_rating_city.head(10))

# Calculate average rating by country
average_rating_country = df.groupby('Country Code')['Aggregate rating'].mean().sort_values(ascending=False)
print(average_rating_country.head(10))

# Plot average rating by city
plt.figure(figsize=(10,6))
sns.barplot(x=average_rating_city.head(10), y=average_rating_city.head(10).index, palette='coolwarm')
plt.title('Top 10 Cities by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('City')
plt.show()