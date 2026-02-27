a = int(input("Enter 1st subject marks: "))
b = int(input("Enter 2nd subject marks: "))
c = int(input("Enter 3rd subject marks: "))
d = int(input("Enter 4th subject marks: "))
e = int(input("Enter 5th subject marks: "))

per = ((a + b + c + d + e)*100)/500
print("Your percentage is: ", per)

if per >= 90:
    print("You got A Grade")
elif per >= 80:
    print("You got B Grade")
elif per >= 70:
    print("You got C Grade")
elif per >= 40:
    print("You got D Grade")
else:
    print("You couldn't pass the exam")

