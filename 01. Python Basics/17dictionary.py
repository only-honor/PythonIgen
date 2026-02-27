'''teachers = {
    "Kaushal": "CSE",
    "Karen" : "Socialogy",
    "Harpreet": "Mathematics",
    "Abha" : "Legal Studies"
}
print(teachers["Karen"])

print(teachers.values())
print(teachers.keys())

for item in teachers:
    print(item, ':', teachers[item]) 


#OPERATIONS IN DICTIONARIES

#Adding & Updating:
cars = {
    'Verna': 1000000,
    'fortuner': 4000000,
    'Breeza': 700000

}
print(cars)
cars['Thar'] = 1500000
print(cars)
cars['Verna'] = 2000
print(cars)

#Program: WAP to create a dictionary in which name as key & no. of wins as values

# Note: key and value aren't keywords
n = int(input("Enter Number Of Students: "))
d = {}
for item in range(n):
    key = input("Enter Name: ") 
    value = int(input("Enter No. of Wins: "))
    d[key] = value

print("The Current dictionary is : ", d)
#By default key is in string so no need to mention strings while adding input. But mention strings with its value if its a string.
'''


teachers = {
    "Kaushal": "CSE",
    "Karen" : "Socialogy",
    "Harpreet": "Mathematics",
    "Abha" : "Legal Studies",
    "Raman" : "Geography",
    "Ratan" : "History"

}
'''
#deleting & pop() : Both are same
del teachers["Karen"]
print(teachers)

teachers.pop("Abha")
print(teachers)

Colors = {
    "Red" : 15,
    "Green" : 20
}
print(Colors)
# Colors.pop("Green")
# Colors.pop("Red")
# print(Colors) #Leaves Empty Dictionary

del Colors["Green"]
del Colors["Red"]
print(Colors) #Also leaves empty dictionary
'''
#Checking existence:
print('Karen' in teachers)
print('emp' in teachers)







