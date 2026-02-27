#Scope: Scope defines the access of variables throughout the program. It is of 2 types: local & global.
#Global: Can accessed throughout the the program at anywhere.
#Local: Can only be accessed inside the block where it is declared ie function, loops or if-else.

#Heirarchy: In nested blocks, the inner blocks can access outer variables while outer blocks can't access variables declared in inner blocks.

#Clash: if we use same variable name as global as well as local scope then inside block, we have to use global keyword when we are dealing with global keyword

x = 300

def sum(a):
     x = 2
     return x + a #will give proiority to x=2 ie local value

print(sum(1))

def greetings(name):
     a = 'Hello '
     def greet():
          print(a + name)
     greet() #Func. call is important

greetings("Arsh")
