num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))

print("Choose operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")

ch = int(input("Enter your choice : "))
if(ch==1):
    print("Sum is %s" %(num1+num2))
elif(ch==2):
    print("Difference is %s" %(num1 - num2))
elif(ch==3):
    print("Product is %s" %(num1 * num2))
elif(ch==4):
    print("Quotient is %s" %(num1/num2))
elif(ch==5):
    print("Remainder is %s" %(num1 % num2))