n =int(input("enter the number"))
res=0
while(n>0):
    digit=n%10
    res=res+digit**3
    n//10
print(res)

