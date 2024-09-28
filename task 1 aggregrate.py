import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Dataset .csv')

# Analyze the distribution of the target variable "Aggregate rating"
sns.histplot(df['Aggregate rating'], kde=True)
plt.title('Distribution of Aggregate Rating')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.show()

# Check for class imbalance
rating_counts = df['Aggregate rating'].value_counts()
print("Class Distribution of Aggregate Rating:\n", rating_counts)

# Visualize class distribution
sns.countplot(x='Aggregate rating', data=df)
plt.title('Class Distribution of Aggregate Rating')
plt.show()
