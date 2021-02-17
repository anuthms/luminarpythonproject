from re import *
phoneno=input("ente phone nunber")

rule="(91)?[0-9]{10}"

matcher=fullmatch(rule,phoneno)
if matcher==None:
    print("invaid no ")
else:
    print("valid no ")