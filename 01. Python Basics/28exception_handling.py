'''
#try-except-finally: Used to handle custom errors also called name errors
 #Executes try block, if error is there then executes except block
try:
    print(x) 
except:
    print("Error Occured")
'''

'''
#many exceptions:
try:
    print(x)
except NameError: #If we do not use NameError keyword, we won't be able to use multiple except blocks
    print("Variable not defined")
except:
    print("Something Else went wrong")
'''


'''
#Else: block executes if no error is there in try block
try:
    print("Hello")
except:
    print("Something went wromg")
else:
    print("All Good") 
'''



'''
#Finally: This block will execute no matter even if error is there in try block or not
try:
    print("x")#print(x)
except:
    print("Variable Not defined")
finally:
    print("Spiderman")
'''

'''
#Raise exception keyword: Other way to handle exception using if block
n = -1
if n<0:
    raise Exception("Sorry")
'''



#Raise typeError: This keyword is used to handle exceptions due to wrong datatype.
x = 'hello'
if not type(x) is int:
    raise TypeError("Only integers are allowed")


