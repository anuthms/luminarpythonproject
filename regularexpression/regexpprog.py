#first should be a alphabet a-k
#number divisible by 3
#third : any character

from re import *
varname=input("enter variable name")

rule="[a-k][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,varname)
if matcher==None:
    print("invalid  variable name")
else:
    print("valid variable")