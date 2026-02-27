# program
line = input("Enter a Line: ")
lowerCount = 0
upperCount = 0
alphaCount = 0
digitCount = 0
spaceCount = 0

for ch in line:
    if ch.islower():
        lowerCount += 1
    elif ch.isupper():
        upperCount += 1
    elif ch.isspace():
        spaceCount += 1
    else:
        digitCount += 1
    if ch.isalpha():
        alphaCount += 1

print("Number Of:")
print("Uppercase = ", upperCount)
print("Lowercase = ", lowerCount)
print("Alhphabets = ", alphaCount)
print("Spaces = ", spaceCount)
print("Digits = ", digitCount)

