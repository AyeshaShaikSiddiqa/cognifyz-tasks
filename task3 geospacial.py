import pandas as pd
import folium
df = pd.read_csv('Dataset .csv')
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)

for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(m)

# Display the map
m.save('map.html')
