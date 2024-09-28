import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Dataset.csv')

# Calculate the percentage of restaurants that offer table booking
table_booking_percentage = df['Has Table booking'].value_counts(normalize=True) * 100
print("Percentage of Restaurants Offering Table Booking:\n", table_booking_percentage)

# Calculate the percentage of restaurants that offer online delivery
online_delivery_percentage = df['Has Online delivery'].value_counts(normalize=True) * 100
print("Percentage of Restaurants Offering Online Delivery:\n", online_delivery_percentage)

# Compare average ratings for restaurants with and without table booking
avg_rating_with_table_booking = df[df['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
avg_rating_without_table_booking = df[df['Has Table booking'] == 'No']['Aggregate rating'].mean()
print(f"Average Rating with Table Booking: {avg_rating_with_table_booking}")
print(f"Average Rating without Table Booking: {avg_rating_without_table_booking}")


# Analyze availability of online delivery across different price ranges
online_delivery_by_price = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack() * 100

print("Online Delivery Availability by Price Range:\n", online_delivery_by_price)

# Optional: Visualize the availability of online delivery across price ranges
online_delivery_by_price.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('Online Delivery Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Percentage of Restaurants')
plt.show()
