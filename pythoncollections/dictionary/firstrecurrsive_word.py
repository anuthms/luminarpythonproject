pattern="ABABBAC"
#recursive character
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1

for key,value in dict.items():
    print(key,",",value)

print(dict)
data=sorted(dict,key=dict.get)
print(data)
