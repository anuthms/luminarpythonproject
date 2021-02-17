pattern="ab"
from re import *
matcher=finditer(pattern,"ababababbbbbababa")
cnt=0
for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print(cnt)