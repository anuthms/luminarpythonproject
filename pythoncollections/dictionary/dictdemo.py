expenses={"jan20":30000,"feb20":28000,"march":30000,"april":40000}
print(expenses["feb20"])
print("june20" in expenses)
expenses["june20"]=25000
print(expenses)
print("march"in expenses)
expenses["march"]-=3000
print(expenses["march"])