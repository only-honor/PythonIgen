import numpy as np
from scipy.optimize import root


def eq(x):
    return (x + np.cos(2*x))
#   return (x + np.cos(x))
#    return (x + 2*np.cos(x))

y = root(eq,0)
print(y.x)
print(y)



# import scipy
# from scipy.optimize import minimize

# def eq(x):
#     return (x**2+x+2)

# y = minimize(eq,1, method = 'BFGS' )
# print(y.x)