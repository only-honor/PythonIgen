
'''
x = {'A', 'B', 'C'}
#Sets are unordered collection of elements. No indexing is there.

#Set Methods:

#len()
print(len(x))

#type()
print(type(x))

#Constructor:
car = ("Verna", "fortuner", "breeza") #Tuple
print(type(car))
z = set(car) # or set(("Verna", "fortuner", "breeza"))
print(z)
print(type(z))

#Traversing
for item in x:
    print(item)

#Membership Operator:
print('B' in x)
print("z" in x) 

#Adding new Element:
x.add("fruit")
print(x)

#pop(): Removes last element
print(x.pop()) #Also prints the popped element ALSO simple x.pop() can be used
print(x)

#Add 2 sets:
car = {"Verna", "fortuner", "Breeza"}
Nums = {22, 33, 55}
car.update(Nums)
print(car)

#remove() or discard()
b = {'sparrow', 'pigeon', 'peacock', 'penguin', 'parrot'}
print(b)
b.remove('peacock')
print(b)
b.discard('pigeon')
print(b)
'''
#-----------------------------------------------------------------------------#

'''
#Join: combines sets using union
s1 = {"A", "B", "C", "D"}
s2 = {'a', 'b', 'c', 'd'}
s3 = s1.union(s2) #Only applicable if 3rd variable is used, otherwise use update()
print(s3)

# s1.update(s2)  #Returns combined values of both sets without using 3rd variable
# print(s1)


#Intersection: returns common values in both sets
s4 = {1, 2, 3, 4, 5}
s5 = {3, 4, 5, 6, 7}

#s6 = s4.intersection(s5)
#print(s6)
s4.intersection_update(s5)
print(s4) #Returns common values in both sets without using 3rd variable

#Symmetric: Returns non-common values
# s7 = s4.symmetric_difference(s5)
# print(s7)

s4.symmetric_difference_update(s5) #RETURNS UNCOMMON VALUES WITHOUT USING 3RD VARIABLE
print("Symetric Values: ", s4)
'''
#----------------------------------------------------------------------------#

