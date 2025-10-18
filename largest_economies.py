import pandas as pd
import numpy as np

# URL of the webpage containing GDP data
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Extract all tables from the webpage
tables = pd.read_html(URL)

# Select the 3rd table (index 2) which contains GDP data
df = tables[3]

# Replace column headers with numbers for easier selection
df.columns = range(df.shape[1])

# Keep only the relevant columns: Country (0) and GDP (IMF) (2)
df = df[[0, 2]]

# Keep only rows 1 to 10 (top 10 economies)
df = df.iloc[1:11, :]

# Rename columns for clarity
df.columns = ['Country', 'GDP (Million USD)']

# Convert GDP column to integer
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert GDP from Million USD to Billion USD
df['GDP (Million USD)'] = df['GDP (Million USD)'] / 1000

# Round GDP values to 2 decimal places
df['GDP (Million USD)'] = np.round(df['GDP (Million USD)'], 2)

# Rename column to reflect the new unit
df.rename(columns={'GDP (Million USD)': 'GDP (Billion USD)'}, inplace=True)

# Save the DataFrame to a CSV file
df.to_csv("./Largest_economies.csv")
