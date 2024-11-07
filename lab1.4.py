#primes upto n
prime=[]
def isprime(n):
  if (n==1 or n==0):
      return False
  for i in range(2,int(n**0.5)+1):
     if n%i==0:
       return False 
     return True
n=int(input("enter no"))
for i in range (1,n+1):
    if isprime(i):
        print(i)
