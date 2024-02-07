import pandas as pd

# Creating a DataFrame
data = {
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Temperature': [75, 85, 80, 72, 88],
    'Humidity': [50, 45, 60, 55, 40],
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
}

df = pd.DataFrame(data)

# Grouping by the 'City' column
grouped_by_city = df.groupby('City')

# Calculating mean temperature and humidity for each city
mean_values = grouped_by_city.mean()
print("Mean Values for Each City:")
print(mean_values)

# Accessing a specific group (e.g., data for 'New York')
new_york_data = grouped_by_city.get_group('New York')
print("\nData for New York:")
print(new_york_data)

# Applying custom aggregation functions
def custom_aggregation(group):
    return {
        'Average_Temperature': group['Temperature'].mean(),
        'Max_Humidity': group['Humidity'].max(),
        'Total_Days': len(group)
    }

custom_aggregated_data = grouped_by_city.apply(custom_aggregation)
print("\nCustom Aggregated Data:")
print(custom_aggregated_data)
