#Matrix Addition
# x = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
# y = [[0, 10, 11], [12,13,14], [15, 16, 17]] 

# z = [[0 , 0, 0], [0, 0, 0], [0, 0, 0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#                    z[i][j] = x[i][j] + y[i][j]
# for i in z:
#         print(i)





#Row to column
# x = [[8,1,1],[2,0,1],[1,2,1]]
# z = [[0,0,0], [0,0,0],[0,0,0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         z[i][j] = x[j][i]

# #print(z)
# for i in z:
#     print(i)  #Returns matrux Format, the error I was doing was print(z) but print(i) will be there






#Matrix Multiplication

x = [[1,1,2],[1,0,1],[2,3,1]]
y = [[1,2,3,1],[1,1,1,1],[1,2,1,1]]
z = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
         z[i][j] = x[i][k] * y[k][j]

for ch in x:
   print(ch)
for jk in y:
   print(jk)
for l in z:
   print(l)

