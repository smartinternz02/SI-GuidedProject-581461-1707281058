import pandas as pd

# Creating a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, None, 22, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Detecting missing values
missing_values = df.isnull()
print("Missing Values:")
print(missing_values)


# Dropping missing values
df_without_missing = df.dropna()
print("\nDataFrame without Missing Values:")
print(df_without_missing)

# Filling missing values with mean age
mean_age = df['Age'].mean()
df_filled = df.fillna({'Age': mean_age})
print("\nDataFrame with Missing Values Filled:")
print(df_filled)

# Interpolating missing values in the 'Age' column
df_interpolated = df.interpolate(method='linear')
print("\nDataFrame with Interpolated Values:")
print(df_interpolated)

# Replacing specific values (e.g., replacing 'None' with 'Unknown')
df_replaced = df.replace(to_replace=None, value='Unknown')
print("\nDataFrame with Replaced Values:")
print(df_replaced)
