#Polymorphism: Diff. classes having same functions
'''
class India:
    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi")

    def C_type(self):
        print("Developing")

class USA:
    def capital(self):
        print("Washington DC")

    def language(self):
        print("English")

    def C_type(self):
        print("Developed")

ob1 = India()
ob2 = USA()

for country in (ob1, ob2):  
    country.capital()
    country.language()
    country.C_type()

class dog:
    def name(self):
        print("German Shephard")
    def sound(self):
        print("Bark")
    def feature(self):
        print("Sharp Teeth")

class bird:
    def name(self):
        print("Sparrow")
    def sound(self):
        print("Chirp")
    def feature(self):
        print("Wings")

obj1 = dog()
obj2 = bird()

for i in (obj1, obj2):
     i.name()
     i.sound()
     i.feature()
'''



class plant():
    def exhale(self):
        print("Release Oxygen")
    def food(self):
        print("CO2")
    def prop(self):
        print("Leaves")

class animal():
    def exhale(self):
        print("CO2")
    def food(self):
        print("O2")
    def prop(self):
        print("Brain")

a = plant()
b = animal()
for ch in (a,b):
    ch.exhale()
    ch.food()
    ch.prop()
