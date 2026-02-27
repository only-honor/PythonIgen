import numpy as np
from numpy import random 

#Split array(): Splits the array
# x = np.array([1,2,3,4,5,6])
# y = np.array_split(x,3)
# print(y)

# a = np.array([23,55,44,33,76]) 
# b = np.array_split(a,3)
# print(b)




# #where():- return indexes, takes array as an argument
# y = np.array([23,44,35,67,89,44,54,31,44,98,76,44])
# #print(np.where(y==44)) #return indexes of 44 in the form of array
# z = np.where(y%2==0) #we can store this method in a variable 
# print(z) #return indexes of even no.s



# # SORT(): sorts the array and takes array as an argument.
# x = np.array([34,56,77,65,56,66,1,34,55,2,67,3,89,4,90,5,25,0])
# print(np.sort(x))
# y = np.sort(x) #returns the same
# print(y)




# # FILTER: We create a corresponding list of boolean, True value corresponding to the array will be printed
# x = np.array([22,33,4,566,76,443,23])
# y = [True, False, True, True, False, False, True]
# print(x[y])
# print(type(x))
# print(type(y))
# z = [True,False]
# print(x[z]) #Will give error as size of z != size of x




#Random Numbers
# x = random.randint(100) #Passing range of 0 -100
# #x = random.randint(-100) #can't pass range<=0

# print(x) #prints Random no. between 0 & 100

# y = random.randint(100, size = (5)) # Will return 5 int numbers
# print(y) #Returns list of 5 random no.'s



# Error: x = random.rand(100) 
# x = random.rand() #returns 1 random no. b/w 0 & 1
# print(x)


# y = random.rand(size = (5)) #won't work here
# print(y)

# z = random.randint(100, size = (2,3))
# print(z) #Returns a matrix of 2 X 3, and range of elements will be b/w 0 & 100



#Random Data distribution:- Assigns probabilities (p) to the elements of array
x = random.choice([3,5,7,9],
p = [0.1,0.3,0.6,0.0],
size = (10))
print(x)
#Note:- size pf p & x must be same. assign 0.0 to those array elements whose occurence you don't want, size defines the no. of times the elements gets to print w.r.t their probabilities. p defines probability