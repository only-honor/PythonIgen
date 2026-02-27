num = int(input("Enter the Number: "))


if num % 7 == 0 and num % 9 == 0:
    print("Number is divisible by both 7 and 9")
elif num % 7 == 0:
    print("Number is divisible by 7")
elif num % 9 == 0:
    print("Number is divisible by 9")
else:
    print("Number is neither divisible by 7 nor divisible by 9")
