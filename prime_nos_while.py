def prime(n):
    num = 2
    f = 0
    while(num < n):
        if(n % num == 0):
            f=1
            num+=1
            break
    if(f==0):
        return True
    else:
        return False

lim = int(input("Upto what numbers do you want to print the prime numbers? "))
i = 1
while(i < lim):
    if(prime(i)):
        print(i)
    i+=1