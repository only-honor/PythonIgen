import numpy as np

#Traversing Operations
'''
a = np.array([44,52, 63, 44, 75])
print(a[0])
print(a[1])
print(a[2])
print(a[2] + a[3])

#Printing 2nd element on 1st row, remember indexing starts from 0
b = np.array([[1,2,3,0], [5,6,8,9]])
print(b[0,1])

#5th element on 2nd row
b = np.array([[25, 45, 67,89,65,44, 1], [11,22,34,55,77,555,33]]) #Make sure no. elements in row and colums must be same as it may give error
print(b[1,4])

#3rd element of 2nd array of first array
c = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(c[0,1,2]) #1st array then 2nd array of 1st array then 3rd element ie we go from outside to inside. First understand ques then code

#last element of 2nd dimension
d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(d[1,-1])
'''


#Index Slicing:
#Syntax = [start:end:step]

e = np.array([23,45,66,44,78,90,21])
print(e[1:5])
print(e[4:])
print(e[:4])
print(e[-3:-1])
print(e[1:5:2])
print(e[::2])



