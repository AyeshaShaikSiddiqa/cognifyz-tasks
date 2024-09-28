import pandas as pd

df = pd.read_csv('Dataset.csv')

df = df.dropna(subset=['Cuisines', 'Aggregate rating'])

df['Cuisines'] = df['Cuisines'].apply(lambda x: [c.strip() for c in str(x).split(',')])

# Explode the dataframe so each cuisine gets its own row
df_exploded = df.explode('Cuisines')

cuisine_rating = df_exploded.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
cuisine_rating = cuisine_rating.sort_values(by='Aggregate rating', ascending=False)

print("Cuisines with highest average ratings:\n", cuisine_rating.head())

cuisine_votes = df_exploded.groupby('Cuisines')['Votes'].sum().reset_index()
cuisine_votes = cuisine_votes.sort_values(by='Votes', ascending=False)

print("\nMost popular cuisines based on votes:\n", cuisine_votes.head())


cuisine_analysis = pd.merge(cuisine_rating, cuisine_votes, on='Cuisines')
cuisine_analysis = cuisine_analysis.sort_values(by='Aggregate rating', ascending=False)

print("\nCuisines with the highest average ratings and their vote counts:\n", cuisine_analysis.head())

import matplotlib.pyplot as plt

# Plotting the relationship between votes and average ratings
plt.figure(figsize=(10, 6))
plt.scatter(cuisine_analysis['Votes'], cuisine_analysis['Aggregate rating'], color='blue')
plt.title('Cuisine Rating vs. Popularity (Votes)')
plt.xlabel('Number of Votes')
plt.ylabel('Average Rating')
plt.grid(True)
plt.show()
