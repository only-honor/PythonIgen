import numpy as np
# x = np.array([1,2,3,4,5])
# print(x.dtype)

# y = np.array([11,22,33,44,55,66], dtype = 'S')
# print(y)
# print(y.dtype)

# z = np.array([1,2,3,4,5], dtype = 'i4') #Where 4 is byte and 32 bits
# print(z.dtype)

# a = np.array([1.2,2.3,4.3,4.6,5.8])
# b = a.astype('i')
# print(a)
# print(a.dtype)
# print(b)
# print(b.dtype)

c = np.array([90.5,5.6,4.3,5.4,2.1,3.3])
d = c.astype('O')
print(d)
print(d.dtype)