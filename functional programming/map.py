lst=[1,2,3,4,6]#square
sqlist=list(map(lambda num:num**2,lst))
print(sqlist)

res=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(res)
#filter

odd=list(filter(lambda num:num%2==0,lst))
print(odd)
even=list(filter(lambda num:num%2!=0,lst))
print(even)
name=["anu","ann","india","aus"]
upplist=list(map(lambda name:name.upper(),name ))
print(upplist)
acountry=list(filter(lambda name:name[0]=="a",name))
print(acountry)

#reduce
from functools import reduce
lst1=[10,20,30,40]
sum=reduce(lambda no1,no2:no1+no2,lst1)
print(sum)
high=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst1)
print(high)
low=reduce(lambda no1,no2:no1 if no2>no1 else no2,lst1)
print(low)
