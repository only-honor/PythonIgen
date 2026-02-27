import numpy as np

x = np.array([1,2,3,4,5])


a = x.copy()
a[0] = 5665
x[3] = 1001
#print(x)
#print(a)



b = x.view()
b[0] = 619
x[3] = 454
#print(x)
#print(b) #Both prints same value

#Base(): Checks if the its copy or view
print(a.base) #Returns none
print(b.base) #Returns array