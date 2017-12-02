import sys

with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Strip \n and stuff from the lines
data = [s.strip() for s in data]

checksum = 0

for line in data:
    splitted = line.split(" ")
    lowest = sys.maxsize
    highest = 0
    for i in splitted:
        i = int(i)
        if i > highest:
            highest = i
        if lowest > i:
            lowest = i

    print("Highest:", highest, "Lowest:", lowest)
    difference = highest - lowest

    checksum += difference

print("Checksum:", checksum)
