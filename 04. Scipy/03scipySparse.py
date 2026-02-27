import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0,0,0,0,0,1,1,0,2])
#print(csr_matrix(arr)) #Returns non zero values with row, column ie (row, column)


#FOR 2D
arr1 = [[0,0,0],[0,0,5],[6,0,7]]
#print(csr_matrix(arr1)) #Returns non-zero values with coordinates(row,column)
#print(csr_matrix(arr1).data) #returns array obj of non zero values(u can check type)

# y = csr_matrix(arr1)
# y.eliminate_zeros() #Remove zeroes
# print(y)

#print(csr_matrix(arr1).sum_duplicates)

print(csr_matrix(arr1))
print("Hello")
print(csr_matrix(arr1).tocsc())

#Install Python, Numpy, Pandas, Scipy

