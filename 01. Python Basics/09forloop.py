'''# Even, odd, sum , table, 
print("Printing 1 to 10....")
for i in range (1,11):
    print(i)

#Even
print("Printing Even...")
for i in range (0,11,2):
    print(i)

#Odd
print("Printing odd...")
for i in range (1,11,2):
    print(i)

#Table
print("Printing Table...")
n = 7
for i in range (1,11):
    print( n, "x", i, "=", n * i)

#Sum
print("Printing Sum...")
sum = 0
for i in range (1,11):
    sum = sum + i
print(sum)

#Sum using if-else

for i in range (1,31):
    if i%2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")'''

'''#Sum of a digit
sum = 0
n = 120

while n > 0:
    rem = n % 10
    sum = sum + rem
    n //= 10
print(sum)

#Palindrome
p = 126

rev = 0
while p > 0:
    remainder = p % 10
    rev = (rev * 10) + remainder
    p//=10
print(rev)

#Armstrong
num = 122
n = num
arm = 0

while n > 0:
    rem = n % 10
    arm = arm + (rem * rem * rem)
    n //= 10
if arm == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")'''


n = 1
sum = 0
for n in range (1,11):
    a = int(input("Enter any Number"))
    n = n + 1
    sum = sum + a
print("Sum is: ", sum)
