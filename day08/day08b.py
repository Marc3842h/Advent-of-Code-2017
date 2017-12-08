with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Strip \n and stuff from the lines
data = [s.strip() for s in data]

def is_true(var, operator, number):
    try:
        value = memory[var]

        if operator == ">":
            return value > number
        elif operator == "<":
            return value < number
        elif operator == ">=":
            return value >= number
        elif operator == "<=":
            return value <= number
        elif operator == "==":
            return value == number
        elif operator == "!=":
            return value != number
    except KeyError:
        memory[var] = 0
        return is_true(var, operator, number)

memory = {}

highest_while_process = 0

for line in data:
    instructions = line.split()

    variable = None
    action = None
    value = None

    variable_to_be_checked = None
    operator = None
    number_to_be_compared = None

    for index, instruction in enumerate(instructions):
        if index == 0:
            # Variable to be modified
            variable = instruction
        elif index == 1:
            # Action to be applied to variable
            if instruction == "inc":
                action = +1
            elif instruction == "dec":
                action = -1
        elif index == 2:
            value = int(instruction)
            # Value to be applied on variable
        elif index == 3:
            # if (ignored)
            print("if.")
        elif index == 4:
            # Compare
            variable_to_be_checked = instruction
        elif index == 5:
            # Operator
            operator = instruction
        elif index == 6:
            # Number to be compared
            number_to_be_compared = int(instruction)

    if is_true(variable_to_be_checked, operator, number_to_be_compared):
        try:
            _ = memory[variable]
        except KeyError:
            memory[variable] = 0

        if action == +1:
            memory[variable] += value
        elif action == -1:
            memory[variable] -= value

        if memory[variable] > highest_while_process:
            highest_while_process = memory[variable]

highest = 0

for key, value in memory.items():
    if value > highest:
        highest = value
    print(key + ":", value)

print("Highest:", highest)
print("Highest ever while processing:", highest_while_process)
