import array

data = None

with open("input.txt", "r") as input_file:
    data = input_file.read().replace("\n", "")

print("Received data from input file:", data)

lastDigit = -1
firstDigit = -1
arrayList = array.array('i')

for number in data:
    print("Character:", number)
    if lastDigit is not -1:
        if lastDigit == int(number):
            arrayList.append(int(number))
            lastDigit = int(number)
        lastDigit = int(number)
    else:
        lastDigit = int(number)
        firstDigit = int(number)

if lastDigit == firstDigit:
    arrayList.append(int(firstDigit))

print(arrayList)

result = 0

for resultNumber in arrayList:
    result = result + resultNumber

print("Result:", result)
