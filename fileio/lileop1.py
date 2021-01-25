#read
#writ
#appened
#
#test test
#1: reference
#f=open("filepath","mode")

f=open("demo.py","r")
word=[]
for lines in f:
   word.append(lines.split(" "))
print(word)
