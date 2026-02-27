'''#Slicing
str1 = "Powerfull"
print(str1[0:5])
print(str1[-4:-1])

print(str1[0:])
print(str1[-4:])

str2 = "Amazing"
print(str2[0:3] + str2[3: ])

#String Functions
str3 = "i love my country 007"
print(str3)

print(str3.capitalize())

sub = "country"

print(str3.find(sub))
print(str3.find(sub, 0,5))


print("Checking spaces....")
str7 = "Hello World"
str8 = " "
print(str7.isspace())
print(str8.isspace())

print("Checking upper/lowercase.....")
str9 = "dehradun"
str10 = "DEHRADUN"
str11 = "Dehradun"
print(str9.isupper())
print(str10.isupper())
print(str11.isupper())
print(str9.islower())
print(str10.islower())
print(str11.islower())
print(str9.istitle())
print(str10.istitle())
print(str11.istitle())

print(str9.upper())
print(str10.lower())
print(str10.title())

str11 = "My name is seriously funny"
print(str11.startswith("my"))
print(str11.startswith("My"))
print(str11.startswith("My", 3,5))

print(str11.endswith("funny"))
print(str11.endswith("Funny"))
print(str11.endswith("funny", 0,5))'''


#alnum, alpha, digit
str4 = "123abc"
str5 = "123"
str6 = "abc"
print(str4.isalnum())
print(str4.isalpha())
print(str4.isdigit())
print(str5.isalnum())
print(str5.isalpha())
print(str5.isdigit())
print(str6.isalnum())

