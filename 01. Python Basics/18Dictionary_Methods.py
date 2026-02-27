'''teachers = {
    "Kaushal": "CSE",
    "Karen" : "Socialogy",
    "Harpreet": "Mathematics",
    "Abha" : "Legal Studies",
    "Raman" : "Geography",
    "Ratan" : "History"

}

#len()
print(len(teachers))

#clear(): Clears the dictionary & returns empty dictionary
#print(teachers.clear())
teachers.clear()
print(teachers)

#get(): Key as added as argument & it returns its corresponding value but in it original type 

cars = {
    'Verna': 1000000,
    'fortuner': 4000000,
    'Breeza': 700000

}
print(cars.get('Breeza')) #returns 700000 as number

#items(): This method returns all items in dictionary as (key, value) tuple
Menu = {
    'Pizza' : 250,
    'Burger' : 70,
    'Fried Rice': 300,
    'Noodles' : 100
}
myList = Menu.items()
for ch in myList:
    print(ch) #Just print key, value in form of tuples

#keys(): This method returns all keys in dictionary in the form of list
print(Menu.keys()) #Here we get output as list

#values(): This method returns all values fro a dict. in form of list
print(Menu.values())

#update(): This method overrides 2 dictionaries, ie it adds Key:Value from new dictionary to original dictionary, overiding it's original value and adds new keys if keys are different or no common keys are there.
Employee1 = {
    "Name": "Diya",
    "Age" : 25,
    "Salary": 200000
}
print(Employee1)
Employee2 = {
    "Name": "John",
    "Dept" : "Sales",
    "Salary" : 100000
}
Employee1.update(Employee2)
print(Employee1)
'''

#Program to add two lists in one list, such that output is :
#[[list3], Elements of list1, [list2]]
list1 = ['a', 'b', 'c']
list2 = ['h', 'i', 't']
list3 = ['0', '1', '2']

# list1.append(list2) #It adds list2 at last of list1
# list1.insert(0,list3) #It adds list3 at 0th index of list1

# print(list1)

for item in list3:
    list1.append(item)
print(list1)

for item in list2:
    list1.insert(0,item)
print(list1)

