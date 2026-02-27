'''a = [1,2,3,4,5]
b = [6,7,8,9,10]
print(a + b)

c = list(input("Enter List Elements: "))
print(c)

d = input("Enter The Items: ")
print(d.split(",")) '''

'''#LIST MANIPULATION:-
#Append: adds element to existing sequence, doesn't returns new list just manipulates the existing
e = ["bread", "Butter", "Jam", "Milk"]
print(e)
e.append("Doritos")
print(e)

#Updation: Updates the elements
e[1] = "Oil"
print(e)

#Deleting: Deletes a particular element or a range of elements
del e[1:3] #If [m:n], deletion will happen from m to n-1
print(e)

f = [0,1,2,3,4,5] #List is created just like indexes
print(f)
del f[3]
print(f)
del f[3:]
print(f)

#COPY
colors = ['red', 'green', 'blue']
g = colors 
print(colors)
print(g)
print(id(colors))
print(id(g))
#The above is shallow copy, with copy reference/address of memory location is also being passed. Hence changes in list g will also affect list colors
g.append("Lavender")
print(g)
print(colors)

#Hence true way of copying is deep copy
fruits = ['apple', 'oranges', 'banana']
h = list(fruits)
print(fruits)
print(h)
print(id(fruits))
print(id(h))
h.append('Kiwi')
print(h)
print(fruits)

#index(x): Returns index of first occurence of "x" in list
car = ['Toyota', 'honda', 'Hyundai', 'Tata']
print(car.index('Tata'))
num = [1,2,3,4,5]
print(num.index(1))

#Extend: uses list as an argument & added to another list to return a combined list
i = [1,2,3,4,5]
j =[6,7,8,9,10]
print(i.extend(j)) #returns nothing
print(i) # 'i' list is modified

#insert(i,x): adds new element x to a position p in existing list
k = ['apple', 'banana', 'kiwi']
print(k.insert(1, "orange")) #returns nothing
print(k) #returns the expected results

#See operations in list doesn't returns anything. They manipulate or modify existing lists

#pop(): removes last element in a list
l = [1,2,3,4,5,6,7]
print(l.pop()) #Prints the popped element
print(l) #Print final modified list

m = l.pop(0) #removes element at a particular index, manipulates both existing and new list ie l & m
print(l)
print(m)

#Remove(x): remove first occurence of x
n = [0,1,2,3,4,5]
print(n)
n.remove(4)
print(n)
o = ['kiwi', 'apple', 'oranges']
print(o)
o.remove("apple")
print(o)
print(o.remove('kiwi')) #returns nothing, only pop() returns the popped element
print(o)

#clear(): removes all the elements from the list, returns none
p = ['kiwi', 'apple', 'oranges']
print(p)
#print(p.clear()) #returns nothing
p.clear()
print(p)

#unlike del, clear() only deletes elements but empty list still exists, however del completely deletes the list

q = [0,1,2,3,4,5]
r = [6,7,8,9,10]
q.clear()
del r[0:5] #works same like clear() ie returns empty list
print(q)
print(r)
del r
print(q) #returns empty list
print(r) #we will get error that r doesn't exist

#count(x): returns occurence of x in the list

s = [12, 18, 24, 24, 24] 
print(s)
print(s.count(12))
print(s.count(24))
print(s.count(50)) #returns 0 as no occurence

#reverse(): reverse the list in place, returns nothing and takes no argument
t = ['p', 'y', 't', 'h', 'o', 'n']
print(t)
#print(t.reverse()) #returns none
t.reverse()
print(t)
'''

#sort(): same as reverse, modifies existing list & doesn't creates a new list, takes no argument, sort the list "IN PLACE". Returns nothing. Sorting is done in increasing or ascending order

u = ['i', 'e', 'a', 'u', 'o']
print(u)
#print(u.sort()) #returns none but sorting is done
u.sort()
print(u)

u.sort(reverse = True) #performs sorting in descending or decreasing order
print(u)

