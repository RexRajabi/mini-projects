word = input("Enter a word: ")
# it addes every char in the word with every possible key
# keys are between 1 to 57
for shift in range(1, 58):
    result = ""
    for char in word:
        result += chr(ord(char) - shift)
    print(f"Shift {shift}: {result}")