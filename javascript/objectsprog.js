//dictionary//keys
var employee={
    id:1000,name:"aju",desig:"developer",salary:25000
}
//console.log(employee.id);

console.log("gender" in employee);
employee["gender"]="male"
console.log(employee);

for (let key in employee){
    console.log(key);
}