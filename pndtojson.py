import pandas as pd
import json

# Load the CSV data into a DataFrame
df = pd.read_csv('quantum_resulta.csv')

# Process the data here...

# Write the DataFrame to a JSON file
with open('output.json', 'w') as f:
    f.write(df.to_json(orient='records'))
