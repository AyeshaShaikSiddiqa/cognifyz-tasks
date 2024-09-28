import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the dataset
df = pd.read_csv('Dataset.csv')

# 2. Data Cleaning and Feature Engineering
# Drop any rows with missing 'Aggregate rating' (target variable)
df = df.dropna(subset=['Aggregate rating'])

# Encoding categorical variables (you can use OneHotEncoder or pd.get_dummies)
# Example for encoding 'Has Table booking' and 'Has Online delivery'
df['Has Table Booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online Delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

# Create 'Cuisine Count' by counting the number of cuisines
df['Cuisine Count'] = df['Cuisines'].apply(lambda x: len(str(x).split(',')) if pd.notna(x) else 0)

# Extract relevant features (ensure all columns exist)
X = df[['Price range', 'Has Table Booking', 'Has Online Delivery', 'Votes', 'Cuisine Count']]  # Add more features as needed
y = df['Aggregate rating']  # Target variable

# 3. Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Build and Train Models
# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Decision Tree Regressor
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)

# Random Forest Regressor
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)

# 5. Predict on the test set
y_pred_lr = lr_model.predict(X_test)
y_pred_dt = dt_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)

# 6. Evaluate the models
# Calculate Mean Squared Error and R-squared for each model
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

mse_dt = mean_squared_error(y_test, y_pred_dt)
r2_dt = r2_score(y_test, y_pred_dt)

mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

# 7. Print the results
print("Linear Regression Performance:")
print(f"Mean Squared Error: {mse_lr}")
print(f"R-squared: {r2_lr}\n")

print("Decision Tree Regressor Performance:")
print(f"Mean Squared Error: {mse_dt}")
print(f"R-squared: {r2_dt}\n")

print("Random Forest Regressor Performance:")
print(f"Mean Squared Error: {mse_rf}")
print(f"R-squared: {r2_rf}\n")

