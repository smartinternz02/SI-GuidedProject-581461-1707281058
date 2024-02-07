import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Accessing columns
names_column = df['Name']
ages_column = df['Age']
cities_column = df['City']

print("\nNames Column:")
print(names_column)

# Adding a new column
df['Occupation'] = ['Engineer', 'Doctor', 'Artist', 'Teacher']
print("\nUpdated DataFrame with Occupation:")
print(df)

# Descriptive statistics
statistics = df.describe()
print("\nDescriptive Statistics:")
print(statistics)

# Filtering rows based on a condition
young_people = df[df['Age'] < 30]
print("\nYoung People:")
print(young_people)

# Sorting the DataFrame by a column
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nSorted DataFrame by Age:")
print(sorted_df)
