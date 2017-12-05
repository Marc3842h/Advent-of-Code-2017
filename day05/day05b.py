with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Strip \n and stuff from the lines
data = [s.strip() for s in data]
data = list(map(int, data))

#data = [0, 3, 0, 1, -3]

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

    # Now, the jumps are even stranger: after each jump, if the offset was three or more,
    # instead decrease it by 1. Otherwise, increase it by 1 as before.
    if data[copy] >= 3:
        data[copy] -= 1
    else:
        data[copy] += 1

    steps += 1

print("Steps required to exit the list:", steps)
