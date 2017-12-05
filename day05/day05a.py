with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Strip \n and stuff from the lines
data = [s.strip() for s in data]
data = list(map(int, data))

steps = 0
current = 0

while len(data) > current > -1:
    # Jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
    if data[current] == 0:
        data[current] += 1
        steps += 1

    copy = current + 0  # Trick to copy this (Sorry for ghetto way)
    instruction = data[current]

    current += instruction

    # In addition, these instructions are a little strange; after each jump,
    # the offset of that instruction increases by 1. So, if you come across an offset of 3,
    # you would move three instructions forward, but change it to a 4
    # for the next time it is encountered.
    data[copy] += 1

    steps += 1

print("Steps required to exit the list:", steps)
