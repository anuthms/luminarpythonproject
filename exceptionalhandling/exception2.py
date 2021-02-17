lst=[10,20,30]
pos=int(input("enter the position element"))

num1=int(input("num1"))
num2=int(input("num2"))
try:
    res=num1/num2
    print(res)
    print(lst[pos])
except Exception as e:
    print(e.args)