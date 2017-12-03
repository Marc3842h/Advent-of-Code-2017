import math
import sys

with open("input.txt", "r") as input_file:
    data = input_file.read().strip()

data = int(data)

# https://en.wikipedia.org/wiki/Taxicab_geometry
#
# HUGE THANKS TO RASPBIAN FOR THE HELP
#

# y
# ^
# | 65  64  63  62  61  60  59  58  57
# | 66  37  36  35  34  33  32  31  56
# | 67  38  17  16  15  14  13  30  55  ^ DOWN
# | 68  39  18   5   4   3  12  29  54
# | 69  40  19   6  |1|  2  11  28  53
# | 70  41  20   7   8  |9| 10  27  52
# | 71  42  21  22  23  24 |25| 26  51  v UP
# | 72  43  44  45  46  47  48 |49| 50
# | 73  74  75  76  77  78  79  80 |81|
# +------------------------------------> x

# math.sqrt(root)
# 3^3 = 9
# 5^5 = 25
# 7^7 = 49
# 9^9 = 81

# For example:
#
#   Data from square 1 is carried 0 steps, since it's at the access port.
#   Data from square 12 is carried 3 steps, such as: down, left, left.
#   Data from square 23 is carried only 2 steps: up twice.
#   Data from square 1024 must be carried 31 steps.
#

# https://stackoverflow.com/questions/35363811/manhattan-distance-python
def manhattan_distance(start, end):
    return sum(abs(e - s) for s,e in zip(start, end))

for i in range(data, data + 1000):  # Brute
    if math.sqrt(i).is_integer() and i % i == 0:
        print(math.sqrt(i))
        root = math.sqrt(i)

difference = root * root - data
center = (root - 1) / 2  # y
axis = difference - center  # x

print("Diff:", difference, "Center:", center, "Axis:", axis)
print("Distance:", manhattan_distance((0, 0), (axis, center)))
