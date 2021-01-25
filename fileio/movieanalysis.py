f=open("movies.csv","r")
dict={}

for lines in f:
    data = lines.rstrip("\n").split(",")
    movie=data[1].rstrip(" ")
    year =data[2]

    if (year not in dict):
        dict[year] = movie
    else:
        dict[year]+= movie

for k,v in dict.items():
    print(k,">>>>>",v)