#2 alphabetkl
#2 no
#2 alpha
#4 digit
from re import *
vehiclename=input("enter the id name")

rule="kl\d{2}[a-z]{2}\d"

matcher=fullmatch(rule,vehiclename)
if matcher==None:
    print("invaid id ")
else:
    print("valid id ")