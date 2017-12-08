with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Strip \n and stuff from the lines
data = [s.strip() for s in data]

hierarchy = {}

for line in data:
    args = line.split()  # Split without arguments splits whitespace by default.

    name = None
    weight = None
    has_children = False
    children = []

    for index, arg in enumerate(args):
        if index == 0:
            name = arg
            # Name
        elif index == 1:
            weight = int(arg.replace("(", "").replace(")", ""))
            # Weight
        elif index == 2:
            has_children = True
            # -> (ignored)
        else:
            children.append(arg.replace(",", ""))
            # children

    # print("Name:", name, "Weight:", weight, "Has children:", has_children, "Children:", children)

    if name is not None:
        hierarchy[name] = {"weight": weight, "children": children, "is_top": True}

for key, value in hierarchy.items():
    # print(key, value)

    for child in value["children"]:
        hierarchy[child]["is_top"] = False

for key, value in hierarchy.items():
    if value["is_top"]:
        print("Is TOP!", key)
