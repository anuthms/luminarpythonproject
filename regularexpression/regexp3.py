#quatifiers
from re import *

#pattern="a+" #continues a will be grouped exclueding 0 no of(a)
#pattern="a*" #any number of a with o no of a
pattern="a?" #check each a and grouped
pattern="a{2}"#grouped in min  2 a eg:aa aa aa
pattern="a{2,4}"#min 2 and max 4 


matcher=finditer(pattern,"aaaaaabbabbabbaa")
for match in matcher:
    print(match.start())
    print(match.group())