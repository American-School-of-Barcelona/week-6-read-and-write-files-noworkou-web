import sys

# Check arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

# Check extension
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

# Try to open file
try:
    file = open(filename)
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0

for line in file:
    stripped = line.strip()

    if stripped == "":
        continue
    elif stripped.startswith("#"):
        continue
    else:
        count += 1

print(count)