import pandas as pd

# Reading data from a CSV file
df = pd.read_csv('example.csv')

# Writing data to a new CSV file
df.to_csv('output.csv', index=False)
# Displaying the first 5 rows of the DataFrame
print(df.head())

# Accessing a specific row by integer position
row_2 = df.iloc[1]

# Accessing a specific column by label
city_column = df['City']
# Filtering rows based on a condition
filtered_data = df[df['Temperature'] > 80]

# Querying data using a query expression
high_humidity_data = df.query('Humidity > 60')
# Grouping data by the 'City' column
grouped_data = df.groupby('City')

# Calculating mean temperature for each city
mean_temp_by_city = grouped_data['Temperature'].mean()
# Sorting DataFrame by 'Temperature' in descending order
sorted_df = df.sort_values(by='Temperature', ascending=False)

# Concatenating two DataFrames along rows
concatenated_df = pd.concat([df1, df2], axis=0)
# Dropping rows with missing values
df_no_missing = df.dropna()

# Filling missing values with the mean
df_filled = df.fillna(df.mean())
