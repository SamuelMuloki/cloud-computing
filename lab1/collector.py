import json
import requests
import sys

# Check if URL is provided as command-line argument
if len(sys.argv) < 2:
    print("Usage: python collector.py <url>")
    sys.exit(1)

# Get URL from command-line argument
url = sys.argv[1]

# Fetch the JSON data from the URL
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()
except requests.RequestException as e:
    print(f"Error fetching data: {e}")
    sys.exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON data received")
    sys.exit(1)

# Count under and over-utilized servers
under_utilized = sum(1 for value in data.values() if 0 <= value <= 49)
over_utilized = sum(1 for value in data.values() if 50 <= value <= 100)

# Create the result dictionary
result = {
    "under": under_utilized,
    "over": over_utilized
}

# Print the result as JSON
print(json.dumps(result))
