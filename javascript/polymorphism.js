class calc{
    add(){
        console.log("inside no arg method");
    }
    add(num){
        console.log("inside one arg method");
    }
    add(num1,num2){
        console.log("inside two arg method");
    }
}
var cal=new calc()
cal.add(10,20);
