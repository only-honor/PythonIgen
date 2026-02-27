'''
x = lambda a: a+10
print(x(5))

y = lambda a,b,c: a+10+b-9+c
print(y(5,6,7))

z = lambda a,b,c,d: (a**b+c/d)*250-1000
print(z(2,2,3,3))
'''

def myf(n):
    return lambda x:x+n

a = myf(5) #Returns lambda x:x+n like a = lambda x:x+n
print(a(102)) #Normally calling lambda function


 

