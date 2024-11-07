x=int(input("enter no"))
order=len(str(x))
sum=0
temp=x
while temp!='\0':
    digit=temp%10
    sum+=digit**order
    temp=temp//10
if(x==sum):
    print(x,"arm strong")
