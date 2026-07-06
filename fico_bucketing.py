# ==========================================
# TASK 4: BUCKET FICO SCORES
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Create 5 buckets
num_buckets = 5

df['rating'] = pd.qcut(
    df['fico_score'],
    q=num_buckets,
    labels=[5,4,3,2,1]
)

# Display bucket boundaries
boundaries = pd.qcut(df['fico_score'], q=num_buckets)

print("\nBucket Boundaries:")
print(boundaries.cat.categories)

# Calculate Probability of Default
pd_table = df.groupby('rating')['default'].mean()

print("\nProbability of Default by Rating:")
print(pd_table)

# Create rating map
rating_map = df.groupby('rating').agg(
    min_fico=('fico_score', 'min'),
    max_fico=('fico_score', 'max'),
    PD=('default', 'mean'),
    borrowers=('fico_score', 'count')
)

print("\nRating Map:")
print(rating_map)

# Plot PD by Rating
pd_table.plot(kind='bar')
plt.xlabel('Rating')
plt.ylabel('Probability of Default')
plt.title('PD by FICO Rating')
plt.show()

