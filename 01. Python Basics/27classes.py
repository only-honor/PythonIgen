# class hello:
#     def __init__(self, name, address): #init means initialisation
#         self.name = name
#         self.address = address

# h = hello("Arsh", "PTK") #h is an object of class hello
# print(h.name)
# print(h.address)
# h2 = hello("Karen", "LDH") #h2 is also an object
# print(h2.name, h2.address)


# class vehicle():
#     def __init__(x, company, model): #We can also take x instead of "SELF"
#         x.company = company
#         x.model = model
        
# c1 = vehicle("Toyota", "Fortuner")
# c2 = vehicle("Mahindr", "Thar")
# print(c1.model, ":", c1.company)
# print(c2.company, ":", c2.model)
    





# class hello:
#     def __init__(self, name, address): #init means initialisation
#         self.name = name
#         self.address = address

#     def printName(self): #This self is accessing variables
#         print("My name is: ", self.name)

# h1 = hello("Arsh", "PTK")
# h1.printName()
#h1.name = "Ash"
#del h1.address
#print(h1.address)




#Inheritence

# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject

# class student(Teacher):
#         def __init__(self, name, subject):
#              super().__init__(name, subject)
#         Teacher.__init__(self, name, subject)
# h2 = Teacher("Karen", "Physics")

# print(h2.name)

#Pass: In class, if we don't have any content then we can use pass stmt, to avoid executing it. It will skip that class and no errors will be shown.


#Super() can also be used instead of the parent class name


class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info()      # Inherited method
d.sound()