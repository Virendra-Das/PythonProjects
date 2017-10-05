num1, num2 = input("Enter two numbers separated by comma : ").split(",")
num1=int(num1)
num2=int(num2)
print("Entered numbers are \n%s \n%s"%(num1,num2))
ch = int(input("Choose operation\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Remainder\n"))
'''
def switch(ch):
    case = {
        1: add(),
        2: sub(),
        3: multiply(),
        4: div(),
        5: rem()
    }
    return case.get(ch, print("Invalid Selection"))
switch(ch)
def add():
    print("Sum is %s" % (num1 + num2))
    return 0
def sub():
    print("Difference %s" % (num1 - num2))
    return 0
def multiply():
    print("Product is %s" % (num1 * num2))
    return 0
def div():
    print("Quotient is %s" % (num1 / num2))
    return 0
def rem():
    print("Remainder is %s" % (num1 % num2))
'''
def switch(ch):
    case = {
        1: "Sum is %s" %(num1+num2),
        2: "Difference %s" %(num1-num2),
        3: "Product is %s" %(num1*num2),
        4: "Quotient is %s" %(num1/num2),
        5: "Remainder is %s" %(num1%num2)
    }
    return print(case.get(ch, "Invalid Selection"))
switch(ch)