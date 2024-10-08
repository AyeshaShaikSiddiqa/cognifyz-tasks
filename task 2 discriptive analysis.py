import pandas as pd
import numpy as np
df = pd.read_csv('Dataset .csv')
numerical_summary = df.describe()
print("Basic Statistical Measures:\n", numerical_summary)
country_distribution = df['Country Code'].value_counts()
print("Distribution of 'Country Code':\n", country_distribution)
city_distribution = df['City'].value_counts()
print("Distribution of 'City':\n", city_distribution)
cuisine_distribution = df['Cuisines'].value_counts()
print("Distribution of 'Cuisines':\n", cuisine_distribution)
top_cuisines = df['Cuisines'].value_counts().head(10)
print("Top 10 Cuisines:\n", top_cuisines)
top_cities = df['City'].value_counts().head(10)
print("Top 10 Cities with the highest number of restaurants:\n", top_cities)
