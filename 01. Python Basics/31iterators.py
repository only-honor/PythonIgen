'''
#Factorial of a no. :
n = int(input("Enter No.: "))
a = 1
fact = 1
while a<=n:
    fact = fact*a
    a+=1
print("Factorial is: ",fact)



#Fibbonacci Series:
m = int(input("Enter a No.: "))
i = 1
a1 = 0
b = 1
print(a1)
print(b)
while a1<=m:
    c = a1 + b
    print(c)
    a1 = b
    b = c
    i = i+1
'''
'''
#Prime not prime:
n = int(input("Enter Number: "))
if n>0:
    for i in range(2,n):
        if n%i==0:
            print(n, "is not prime")
            break
    else:
        print(n, "is prime")
else:
    print("number is not prime")
'''

'''
#Factorial program using functions:
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        #print(i)
        fact = fact * i
    return fact

num = int(input("Enter No.: "))
sol = factorial(num)
print("Factorial is: ", sol)

'''
'''
#break and Continue: break terminates the program while contine skips that iteration
fruits = ['apple', 'banana', 'cherry', 'dragon fruit', 'guava']
for x in fruits:
    print(x)
    if x == 'banana':
        break

for y in fruits:
    if y == 'cherry':
        continue
    print(y)
'''
'''
#Program
fruits = ['apple', 'banana', 'cherry', 'dragon fruit', 'guava']
color = ['red', 'green', 'blue', 'yellow', 'orange']

for x in fruits:
    for y in color:
        print(x,y)
'''



#program:
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def product(x,y):
    return x*y

def div(x,y):
    return x/y

def mod(x,y):
    return x%y

a = float(input("Enter 1st No.: "))
b = float(input("Enter 2nd No.: "))

print("Choose the operation : ")
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Modulus")
o = int(input("Enter Your Choice: "))

if o == 1:
    print(add(a,b))
elif o ==2:
    print(sub(a,b))
elif o == 3:
    print(product(a,b))
elif o == 4:
    print(div(a,b))
elif a == 5:
    print(mod(a,b))
else:
    print("Invalid Choice!")

