import json
import random
import os

# Generate the data
num_servers = 10
server_data = {f"server{i}": random.randint(1, 100) for i in range(num_servers)}

# Define the path for the output file
output_path = "/var/www/html/data.json"

# Ensure the directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write the JSON data to the file
with open(output_path, 'w') as f:
    json.dump(server_data, f)

print(f"Data has been written to {output_path}")
