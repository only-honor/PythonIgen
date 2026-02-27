import datetime
x = datetime.datetime.now()
#print(x)
#print(x.year)

print(x.strftime("%A")) #Prints Day of the week like Thursday
print(x.strftime("%a")) #prints Day of the week in short like Thu
print(x.strftime("%W")) #prints Day no. of the week (Eg: for thur its 4), range: 0-6, 0 is sunday 
print(x.strftime("%d")) #Prints date in the month, for 29 jan it gives 29
print(x.strftime("%b")) #prints month name in short like jan
print(x.strftime("%B")) #prints full month name like January
print(x.strftime("%m")) #prints Month No. eg: for jan it's 1. Range: 1-12
print(x.strftime("%y")) #prints year in short like 2026 -> 26

