a = 0
b = 1
num = int(input("How many elements do you want in the series? "))
for i in range(0 , num):
    c = a + b
    print(c)
    a = b
    b = c
