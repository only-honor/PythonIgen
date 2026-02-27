import pandas as pd


#DataFrame don't work in std dictionary
marks = {
    "Eng" : 75,
    "Maths" : 80,
    "Physics" : 86,
    "Chemistry" : 82,
    "Information Practices" : 88
}
#print(marks)
#print(pd.Series(marks))


#DataFrame only works if data is passed as ordered pair(list, tuple) in a dictionary amd won't work for dictionary or sets
mark1 = {
    'Subject' : ("Eng","Maths","Physics","Chemistry","Information Practices"),
    'No.' : [75, 80, 86, 82, 88]
}
#print(pd.DataFrame(mark1))
#print(pd.Series(mark1))
#Series & DataFrame are just ways to display data differently

#print(pd.Series(marks, index = ['x', 'y', 'z', 'a', 'b'])) #Will give NaN


p = ['MI', 'CSK', "KKR", 'RR', "PK", "SRH"]
print(pd.Series(p))
#print(pd.Series(p, index = ['a', 'b', 'c'])) #length don't match with p
print(pd.Series(p, index = ['a', 'b', 'c', 'd', 'e', 'f']))
#print(p['f']) #Org p is not changed, WE ARE JUST PRINTING THE CHANGES

m = pd.Series(p, index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(m) #copy of p with changes passed to m
print(m['f'])