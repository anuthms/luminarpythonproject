f=open("covid_19_india.csv","r")
covid={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cured=data[6]
    confirmed=data[8]
    death=data[7]

    if(state not in covid):
       covid[state]={"state":state,"cured":cured,"confirmed":confirmed,"death":death}
    print(covid)
def print_covid_data(**kwargs):
    state=kwargs["state"]
    if (state in covid):
        print(covid[""])
        if ("prop" in kwargs):
            prop = kwargs["prop"]
            print(covid[state][prop])
print_covid_data(state="kerala",prop="cured")