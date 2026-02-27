'''#tuples: Depicted through parenthesis
a = () #Empty tuple
b = (7,) #tuple with 1 member
n = (1,2,3,4,5,4,4)
print(n)
c = [1,2,3,4,5]
print(c)
d = tuple(c) #Type Conversion
print(d)

e = tuple('hello')
print(e)

#INPUT FROM USER FOR TUPLE
f = tuple(input("Enter: "))
print(f)

# g = ()
# for ch in g:
#     if len(g) < = 3:


h = eval(input("Enter values: ")) #Evaluation
print(h)

#Some operations:: len(), index(), slicing[:], membership(in/not in), concatenation(+), Replication(*), immutability

#Traversing
tupl = ('p', 'y', 't', 'h', 'o', 'n')
for ch in tupl:
    print(ch) #Print(t[ch]) is wrong

#Joining or Concatenation
j = (1,2,3,4,5)
k = (6,7,8,9,10)
print(j+k)

#Repeating or Replicating: Uses * operator to print it multiple times
print(j * 3)

#Slicing: Same as previous ones, in tuple[m:n] it prints from m to n-1
l = (0,1,2,3,4,5)
print(l[1:4])
#In slicing, [m:n:steps], there is steps option too, which can only be skipped if its value is 1, do not skip steps for any other no. not even -1.





m = [23,45,67,89,34,56,78,12,34,56,65,43,46,35,67]
print(m)
print(m[::-1]) #Reverse
print(m[0::2]) #Even indexes or m[::2]
print(m[1::2]) #Odd indexes
print(m[::3]) #starts from 0 to the end, and prints every 3rd element or skip 2 in between

#METHODS: length(), min(), max(), count(), index(), zipped()
print(len(m)) #Tuple itself is passed as argument
print(max(m)) #Tuple itself is passed as argument
print(min(m)) #Tuple itself is passed as argument
print(m.count(67)) #Element of tuple is passed as argument, returns occurences of that element in tuple
print(m.index(56)) #Element of tuple is passed as argument, returns index no. of that element in tuple


#zipped() : Converts multiple tuples into zip file
n = (1,2,3)
o = ('a', 'b', 'c')
p = ([45,56,78])

q = zip(n,o,p) # n, o and p converted to zip whose file name is q
print(q) #Prints memory location of zipped file "q"
newtuple = tuple(q)  #Zipped file q is extracted
print(newtuple)




#Packing & Unpacking: creating tuple from list of values is packing & its reverse ie extracting values from tuple is unpacking

#Unpacking: uses "-" as unpacker or separater
s = (1,2,3,4)
print(s)
s1,s2,s3,s4 = s #Declare new variables depending on no. of elements in tuple
print("Unpacked Tuple: ", s1, "-", s2, "-", s3, "-", s4) 
#or print(s1, "-", s2, "-", s3, "-", s4)
'''
g = []
a = 0
while a <= 5:
    b = int(input("Enter No. : "))
    g.push(b)
    a += 1
print(tuple(g))


  

    

