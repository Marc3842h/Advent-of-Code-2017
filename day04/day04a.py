with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Strip \n and stuff from the lines
data = [s.strip() for s in data]

count = 0

for line_index, line in enumerate(data):
    splitted_line = line.split()
    splitted_set = set(splitted_line)  # A set can not contain duplicate values.

    if len(splitted_line) == len(splitted_set):
        count += 1


print("Amount of non duplicates:", count)
