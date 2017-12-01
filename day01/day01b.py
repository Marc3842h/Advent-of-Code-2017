import array

data = None

with open("input.txt", "r") as input_file:
    data = input_file.read().replace("\n", "")

print("Received data from input file:", data)

index = 0
length = len(data)
arrayList = array.array('i')

for number in data:
    number = int(number)
    print("Character:", number)
    try:
        nextValid = int(data[index + (length / 2)])
        print("Next valid:", nextValid)
        if nextValid == number:
            arrayList.append(nextValid + number)

    except IndexError:
        continue

    index += 1

print(arrayList)

result = 0

for resultNumber in arrayList:
    result = result + resultNumber

print("Result:", result)
