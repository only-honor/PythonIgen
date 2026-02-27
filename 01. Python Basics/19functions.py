#Functions are of 3 types:
#Builtin functions
#Functions in modules
#User-defined Functions


'''def calc(x,y):
    return x+y, x-y, x*y,x/y,x%y

a = float(input("Enter No. 1: "))
b = float(input("Enter No. 2: "))
#calc(a,b)
#print(calc(a,b))

#Better way:
add, sub, product, div, mod = calc(a,b)
print("Sum = ", add)
print("Subtraction = ", sub)
print("Product = ", product)
print("Division = ", div)
print("Modulo = ", mod)


#Principal, rate, time:
def simpInt(principal, rate, time):
    return (principal*rate*time)/100


p = int(input("Enter Principal Amount: "))
q = int(input("Enter Rate of Intrest: "))
r = int(input("Enter Time Period: "))

print("Simple Interest: ", simpInt(p,q,r))


#We can also put default values in args:

def simpInt(principal, rate = 10/100, time = 2 ):
    return principal * rate * time
#there is 10/100 with rate as it represents 8% hence S.I becomes p*r*t not (p*r*t)/100 as / 100 is already passed with rate as args


z = int(input("Enter Principal: "))
print("Simple Interest is: ", simpInt(z))

#Retuen values from functions
#Func. can return 3 things: 
#literals: constants like 1,2,3,
#Variables: like we saw in simple interest example
# expressions: same like simple interst example
'''

#Program: To find marks & Grades

def percentage(s1,s2,s3,s4,s5):
    per = ((s1+s2+s3+s4+s5)/500)*100
    return per

a = float(input("Enter marks of subject 1: "))
b = float(input("Enter marks of subject 2: "))
c = float(input("Enter marks of subject 3: "))
d = float(input("Enter marks of subject 4: "))
e = float(input("Enter marks of subject 5: "))

p = percentage(a,b,c,d,e)
print("You got ", p, "%")

if p >= 90:
    print("You got A Grade")
elif p>= 75:
    print("You got B Grade")
elif p>= 60:
    print("You got D Grade")
elif p >= 40:
    print("You got E Grade")
else:
    print("You could n't pass the exams")

