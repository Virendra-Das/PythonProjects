username = "Virendra"
print("Hello %s!"%username)
team = "Quest"
manager = "Neerav"
print("Your team is %s and your manager will be %s"%(team,manager))

#%s can also be user with list
mylist = [1,2,3]
print(mylist)
print("The list : %s"% mylist)

#Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string+" %s %s. Your balance is $%s" %data)
print(format_string," %s %s. Your balance is $%s" %data)
#comma while concatenating adds a space

astring = "Hello World!"
print(len(astring))
print(astring.lower())
print(astring.upper())
print(astring.count('o'))
#count() is case sensitive
print(astring.count('O'))

#slicing
print(astring[2:]) #specified index to last
print(astring[:7]) #start to 1 less than specified index
print(astring[2:7]) #start index to 1 less than end index
print(astring[2:7:1]) #start index to end index stepping 1 element at a time
print(astring[::1]) #start to index stepping 1 element at a time
print(astring[::2]) #start to index stepping 2 element at a time
print(astring[::-1]) #reversing the string- start to end stepping -1 elements at a time
print(astring[-1::-1]) #reversing the string - start from last and step -1 elements each time
print("This is just to test commit from git")

#Some functions
astring = input("Enter a string : ")
print(astring.startswith("Hello"))