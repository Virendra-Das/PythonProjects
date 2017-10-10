x = 2
print(x==2)
print(x==3)
print(x<3)
print(type(print(x==3)))

choice = int(input("Enter 1 : "))
if(choice == 1):
    print("You Entered 1")
else:
    print("You did not enter 1")

name = input("Enter username : ")
if(name in ["virendra" , "prasuk" , "avdhesh" , "vaibhav"]):
    print("You are authorised to access the wifi")
else:
    print("Unauthorised user")


name = input("Enter username : ")
if(name.lower() in ["virendra" , "prasuk" , "avdhesh" , "vaibhav"]):
    print("Hi %s" % name+". You are authorised to access the wifi")
else:
    print("Unauthorised user")