from  re import *
#check for either a or b
#pattern="[abc]"
#pattern="[a-z]"#will check for lowercsae a toz
#pattern="[A-Z]"
#pattern="[a-zA-Z]"BOTH UPPER AND LOWER
#pattern="[0-9]"check for digits
#pattern="[^0-9]" #except 0-9
#pattern="[a-zA-Z0-9]"#all is possiable
#matcher=finditer(pattern,"abCD765efyz")
#for match in matcher:
#    print(match.start())
#    print(match.group())

pattern="\s" #check for space
pattern="\d" #check for digit
pattern="\D" # [^0-9] except digit
pattern="\w"#all words except special character eg:@$
pattern="\W"#except words