with open("input.txt", "r") as input_file:
    data = input_file.readlines()

# Strip \n and stuff from the lines
data = [s.strip() for s in data]

count = 0

# https://stackoverflow.com/questions/38138842/how-to-check-whether-two-words-are-anagrams-python
def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

for line_index, line in enumerate(data):
    splitted_line = line.split()
    valid_line = True

    for word_index, word in enumerate(splitted_line):
        for word_index2, word2 in enumerate(splitted_line):
            if word_index != word_index2:
                if is_anagram(word, word2):
                    print("Found anagram in line", str(line_index) + ":", word)
                    valid_line = False

    if valid_line:
        count += 1

print("Amount of non-anagrams:", count)
