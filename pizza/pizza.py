mport sys
import csv
from tabulate import tabulate

# Check arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

# Check extension
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

# Read file
try:
    with open(filename) as file:
        reader = csv.reader(file)
        table = list(reader)
except FileNotFoundError:
    sys.exit("File does not exist")

# First row = headers
headers = table[0]
rows = table[1:]

# Print table
print(tabulate(rows, headers=headers, tablefmt="grid"))