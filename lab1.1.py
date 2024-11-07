x=int(input("enter number"))
if x<=1:
    print("not prime")
else:
     prime=TRUE
     for i in range(2,int(x**0.5)+1):
        if x%i==0:
            is_prime=false
            break
if  prime:
    print("is prime")
else:
    print("not prime")