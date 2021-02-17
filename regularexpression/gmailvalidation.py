from re import *
gmailid=input("enter mail id")

rule="[a-z]*[/d]*@gmail.com"

matcher=fullmatch(rule,gmailid)
if matcher==None:
    print("invaid mail id ")
else:
    print("valid mail id ")