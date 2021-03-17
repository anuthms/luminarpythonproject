class Employee{
    constructor (name,id,designation,sal){
        this.name=name;
        this.id=id;
        this.designation=designation;
        this.sal=sal;
    }
    printdetails=()=>{
        console.log(this.name+this.id+this.designation+this.sal);
    }
}
var employee=[]
var obj=new Employee("anu",001,"developer",50000)
var obj1=new Employee("ann",002,"designer",48000)
var obj2=new Employee("ana",003,"developer",52000)
var obj3=new Employee("annie",004,"designer",40000)
employee.push(obj)
employee.push(obj1)
employee.push(obj2)
employee.push(obj3)
//employee.forEach(emp=>console.log(emp.designation));
//employee.map(emp=>emp.sal+2000).forEach(sal=>console.log(sal));
//employee.map(emp=>emp.name.toUpperCase()).forEach(name=>console.log(name));
//employee.filter(emp=>emp.designation=="developer").forEach(emp=>console.log(emp));
//employee.sort((o1,o2)=>o1.sal>o2.sal?-1:1).forEach(emp=>console.log(emp));
let high=employee.map(obj=>obj.sal).reduce((sal1,sal2)=>sal1>sal2?sal1:sal2)
console.log(high);
let low=employee.map(obj=>obj.sal).reduce((sal1,sal2)=>sal1>sal2?sal2:sal1)
console.log(low);