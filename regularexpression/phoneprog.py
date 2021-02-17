from re import *
f=open("phonenumbers.py","r")
phonenumbers={}

rule="(91)?[0-9]{10}"

matcher=fullmatch(rule,phonenumbers)
if matcher==None:
    print("invaid no ")
else:
    print("valid no ")