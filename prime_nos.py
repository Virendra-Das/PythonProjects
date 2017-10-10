def prime(n):
    f=0
    for num in range(2 , n):
        if(n % num == 0):
            f=1
            break
    if(f==0):
        return True
    else:
        return False

lim = int(input("Show prime numbers till what limit? "))
count=0
for i in range(2, lim):
    if(prime(i)):
        print(i)
        count+=1
print("Total %s prime numbers are there in the given range." % count, end='')