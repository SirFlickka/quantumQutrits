import csv

# Our quantum data
quantum_data = [1, 0, 0, 0]

# Open a file in write mode
with open('quantum_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(quantum_data)
