text="hello hai hello hai hello"
#word count
#hello:3, hai:2
words=text.split(" ")
#print(words)
dict={}

for word in words:
    if("hai" not in dict):
        dict[word]=1
    else:
        dict[word]+=1
    print(dict)