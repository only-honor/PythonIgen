import pandas as pd


# print(pd.__version__)
# x = {
#     'Cars': ["BMW", "Volvo", "Ford"],
#     'Passing' : [3,7,2]
# }
# #print(pd.DataFrame(x))

# y = (pd.DataFrame(x))
# print(y)


#Series
# a = [101,7,3]
# b = pd.Series(a)
# print(b) #labels will be 0,1,2 by default
# print(b[0])

# b = pd.Series(a, index = ['x', 'y', 'z']) #labels
# print(b)
# print(b["y"])



#Key-Value object as series
calories = {
    'day1' : 420,
    'day2' : 280,
    'day3' : 390
       }
x = pd.Series(calories)
print(x)


