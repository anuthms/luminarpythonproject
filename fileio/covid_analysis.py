f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    if(state=="Telengana" ):
        state="Telangana"
    confirmed_cases=int(data[8])
    if(state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state ]= confirmed_cases

for k,v in dict.items():
    print(k,">>>>>",v)

result=sorted(dict,key=dict.get,reverse=True)
#print(result[0],dict.get(result[0]))
print(result[0],dict[result[0]])