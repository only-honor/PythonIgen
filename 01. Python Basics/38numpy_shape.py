import numpy as np
#x = np.array([1,2,3,4,5,6])
#x = np.array([[1,2,3,4,5,6], [34,56,77,88,55,33]]) #returns 2 rows 6 col
#x = np.array([1,2,3,4,5,6], ndmin = 5)
#print(x.shape)


#Reshape
#x = np.array([1,2,3,4,5,6])
#print(x.reshape(2,3)) #Reconfigure it in the form of 2X3 matrix

y = np.array([1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,12,13,14,15,16,17])
#print(y.reshape(3,4,2)) #(no of unique matrices, no. of rows, no. of cols)
#(a,b,c): product of them ie a x b x c shouldn't exceed org no. of elements in parent matrix
# for i in y:
# print(i)


#Concatenation
a = np.array(['a', 'b', 'c', 'd'])
b = np.array(['e', 'f', 'g', 'h'])
c = np.concatenate((a,b))
print(c)

