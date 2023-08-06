import pandas as pd
import numpy as np

# Load the CSV data into a DataFrame
df = pd.read_csv('results.csv')

# Convert the DataFrame into a 1D array
data = df.values.flatten()

# Calculate the number of rows needed for the reshaped data
n_rows = int(np.ceil(data.size / 128))

# Pad the data if necessary so it can be reshaped
if data.size % 128 != 0:
    data = np.pad(data, (0, 128 - data.size % 128), constant_values=0)

# Reshape the data into a DataFrame with 128 columns
reshaped_df = pd.DataFrame(data.reshape((n_rows, 128)))

# Now reshaped_df has 128 columns and as many rows as needed to accommodate all the data
reshaped_df.to_json('reshaped_data.json', orient='records')
