import sys

with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Strip \n and stuff from the lines
data = [s.strip() for s in data]

checksum = 0

for line in data:
    splitted = line.split(" ")

    for i in splitted:
        i = int(i)
        valid = 0
        for x in splitted:
            x = int(x)
            if i != x:
                if i % x is 0:
                    print("Found:", i, "/", x, "=", i / x)
                    checksum += i / x


print("Checksum:", checksum)
