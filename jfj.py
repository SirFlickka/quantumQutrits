import pandas as pd

# Read the CSV file
df = pd.read_csv('statese.csv')

# Sort the DataFrame
df = df.sort_values(by=list(df.columns))

# Remove duplicates
df = df.drop_duplicates()

# Save the sorted, deduplicated DataFrame to a new CSV file
df.to_csv('sorted_deduplicated_states.csv', index=False)
