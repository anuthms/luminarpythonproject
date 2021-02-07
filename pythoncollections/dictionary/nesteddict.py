employee={
     1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
     1001:{"id":1001,"name":"roy","salary":30000,"exp":2},
     1002:{"id":1002,"name":"ria","salary":35000,"exp":2},
}
print(employee[1000])
if(1001 in employee):
    print(employee[1001]["name"])
else:
    print("no employe0")

if(1002 in employee):
    print(employee[1002]["salary"])
else:
    print("no employee")

def print_employee(**kwargs):
 #   if id in employee:
 #       print(employee[id]["name"])
#print_employee(id=1002)
    id=kwargs["id"]
    if(id in employee):
       print(employee[id]["name"])
       if("prop"in kwargs):
          prop=kwargs["prop"]
          print(employee[id][prop])
       else:
         pass
    else:
        print("employee without id")
print_employee(id=1002,prop="exp")