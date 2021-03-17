class Parent{
    m1(){
        console.log("inside parent class");
    }
}
class Child {
    m2(){
            console.log("inside child class");
        }
}
class Subchild {
    m3(){
        console.log("inside sub child class");
    }
}
    var child=new Child()
    child.m2();
    child.m1();
    child.m3();
