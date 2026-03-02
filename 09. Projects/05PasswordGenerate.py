import string
import random 

length = int(input("Enter Passwprd Lemgth: "))

character_list = ""

print("Choose your choice: ")
print("Press 1 for password to include Alphabets")
print("Press 2 for password to inclide Digits")
print("Press 3 for password to include special Character")
print("Press 4 to print password")



while(True):
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        character_list += string.ascii_letters
        #print(type(character_list))
    elif choice == 2:
        character_list += string.digits
    elif choice == 3:
        character_list += string.punctuation
    elif choice == 4:
        break
        
    else:
        print("Invalid Choice")

password = []
for i in range(length):
    random_char = random.choice(character_list)
    password.append(random_char)

#print("Password: ")
print("Password: ","".join(password))

        