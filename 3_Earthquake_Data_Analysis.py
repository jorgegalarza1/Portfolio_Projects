# 3_Earthquake_Data_Analysis

# This is only a tool to be used for educational purposes for python coding.

# Data retrieved on 11/29/2022 from 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php'
# Copy and paste this code to your text editor / IDE and start messing around with the data.
# The data used for this analysis represents world earthquake data from the month of November, 2022.
# All code was has a comment on top '#'.
# The graph does not have comments; play with the values and observe what changes, and what parameters change what.

import pandas as pd
import matplotlib.pyplot as plt

# Read csv file that contains all earthquake data in the world that have happened in the last 30 days
# This data is updated every minute
earthquakes = pd.read_csv('all_month.csv')

# Save and print the name of each of the columns
columns = earthquakes.columns
print(columns)

# Print the first 3 rows of the entire dataset
print(earthquakes.head(3))

# Print the last 3 rows of the entire dataset
print(earthquakes.tail(3))

# Save and print number of rows
row_count = earthquakes.shape[0]
print(row_count) # 10154 Rows

# Save and print number of columns
col_count = earthquakes.shape[1]
print(col_count) # 22 Columns

# Or you can get row_count and col_count like this
print(earthquakes.shape)

# Imagine we only want to work with the 'time', 'place' and 'mag'
specific_cols = earthquakes[['time', 'place', 'mag']]
print(specific_cols)
# and from the specific_cols, we are only interested in index 4
print(specific_cols.iloc[4])
# now we're interested indexes 0 to 4
print(specific_cols.iloc[0:5]) # Remember, the second number is always excluded (reason for using 5)
# now we're interested in whatever information is in row in index 2, column in index 1
print((specific_cols.iloc[2,1]))

# Now we want to display row by row for the entire dataset (just the top 3 for simplicity)
for index, rows in earthquakes.head(3).iterrows():
    print(index, rows)
    print(" ") # Just to make it look better

# From the entire dataset, I want only the earthquakes that had magnitude of over 2
higher_than_two = earthquakes.loc[earthquakes['mag'] > 2]
print(higher_than_two)
# Organize column and double-check your work
sort_column = higher_than_two['mag']
print(min(sort_column)) # Minimum entry is 2.0099999. We got it

# We just want to sort in increasing order based on magnitude from the entire dataset
just_mag = earthquakes.sort_values('mag', ascending=True)
print(just_mag.head(3))

# Let's imagine you live in Texas and only care about the Texas earthquakes
only_texas = earthquakes[earthquakes["place"].str.contains("Texas" or "TX")]
print(only_texas)
# Or California
only_cali = earthquakes[earthquakes["place"].str.contains("California" or "CA")]
print(only_cali)

# Between California and Texas, what state had the highest mag earthquake?
highest_tx = only_texas.sort_values('mag', ascending=False)
highest_ca = only_cali.sort_values('mag', ascending=False)
print(highest_ca['mag'])
print(highest_tx['mag'])

# From the only_texas variable we only want the state of Texas and the earthquakes that are higher than 2
texas_over_two = only_texas.loc[only_texas['mag'] > 2]
print(texas_over_two)

# we want to save that new data set as texas_over_two.csv
texas_over_two.to_csv('texas_over_two.csv')

# Load new csv
texas = pd.read_csv('texas_over_two.csv')

# What is the average/mean magnitude for the earthquakes in the state of texas and the average/mean for the whole country (including Texas)
print(only_texas['mag'].mean())
print(earthquakes['mag'].mean())

# What is the average earthquake magnitude per state
avg_per_state = earthquakes.groupby(['locationSource']).mean(['mag'])
print(avg_per_state['mag'])

# Get rid of every character before the comma in the column 'place', that way we can get a less specific address
earthquakes['place'] = earthquakes['place'].str.rsplit(',').str[-1]
print(earthquakes['place'])

# Visualizing earthquakes in the World Over Mag 5.5
earthquakes_5_5 = earthquakes.loc[earthquakes['mag'] > 5.5]
earthquakes_5_5.plot(style = 'seaborn',
                     kind = 'scatter',
                     x = 'mag',
                     y = 'place',
                     c = 'mag',
                     s = 100,
                     alpha = 0.7,
                     )
plt.yticks(rotation = 5, fontsize=9)
plt.title("Earthquakes of the World over Magnitude 5.5", fontsize=24)
plt.ylabel(None)
plt.xlabel("Earthquake Magnitude", fontsize=14)
plt.show()
