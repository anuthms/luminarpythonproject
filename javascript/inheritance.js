class Parent{
    m1(){
        console.log("inside parent class");
    }
}
class Child extends Parent{
    m2(){
            console.log("inside child class");
        }
}


    var child=new Child()
    child.m2();
    child.m1();
   
