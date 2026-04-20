# -------------------------------
# Practical -2
# Data Cleaning, Transformation, and Analysis using Pandas & NumPy
# -------------------------------

# Step 1: Import Libraries
import pandas as pd
import numpy as np


# Step 2: Create Sample Dataset
data = {
    'Name': ['Rasna', 'Amit', 'Neha', 'Pooja', 'Ankit'],
    'Age': [22, np.nan, 25, 24, np.nan],
    'Marks': [78, 85, np.nan, 90, 88],
    'Branch': ['CSE', 'IT', 'CSE', None, 'IT']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)


# -------------------------------
# Step 3: Data Cleaning (FIXED)
# -------------------------------

print("\nMissing Values:\n", df.isnull().sum())

# Proper way (NO inplace, NO chaining issue)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].median())
df['Branch'] = df['Branch'].fillna('Unknown')

# Drop duplicates
df = df.drop_duplicates()


# -------------------------------
# Step 4: Data Transformation (FIXED)
# -------------------------------

# Convert safely to integer
df['Age'] = df['Age'].astype(int)

# Create Result column
df['Result'] = np.where(df['Marks'] >= 40, 'Pass', 'Fail')

# Rename column
df = df.rename(columns={'Marks': 'Score'})

# -------------------------------
# Step 5: Data Analysis
# -------------------------------

# Statistical Summary
print("\nStatistical Summary:\n", df.describe())

# Average Score by Branch
avg_score = df.groupby('Branch')['Score'].mean()
print("\nAverage Score by Branch:\n", avg_score)

# Students Scoring Above 80
high_scorers = df[df['Score'] > 80]
print("\nStudents Scoring Above 80:\n", high_scorers)


# -------------------------------
# Step 6: NumPy Analysis
# -------------------------------

print("\nMax Score:", np.max(df['Score']))
print("Min Score:", np.min(df['Score']))
print("Mean Score:", np.mean(df['Score']))
print("Standard Deviation:", np.std(df['Score']))


# -------------------------------
# Step 7: Final Cleaned Data
# -------------------------------

print("\nCleaned and Transformed Data:\n", df)