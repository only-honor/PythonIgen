import numpy as np
a = np.array([1,2,3,4]) #Converts list into array
print(a)
print(np.__version__)
print(type(a))

b = np.array((1,2,3,4)) #Tuple will also be converted to nd_array object
print(b)

#dimensions 
c = np.array(43)
print(c)
print(c.ndim)
d = np.array([1,2,3,4,5])
print(d)
print(d.ndim)
e = np.array([[1,2,3],[4,5,6]])
print(e)
print(e.ndim)

#3D array:-
f = np.array([[[1,2,3],[4,5,6]], [[11,22,33], [66,77,88]]])
print(f)
print(f.ndim) #Prints dimension of the array

#passing dimension as args
g = np.array([1,2,3,4,5], ndmin = 5) #ndmin gives no. of dimensions 
print(g)
print(g.ndim)

#1st create 2 1d arrays, then make 2 2d arrays and then by closing it becomes 3D
h = np.array([[[1,2,3,4,5], [1,2,3,4,5]], [[1,2,3,4,5],[1,2,3,4,5]]])
print("H = ", h.ndim)