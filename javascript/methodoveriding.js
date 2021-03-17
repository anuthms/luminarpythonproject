class Parent{
    mobile(){
        console.log("parent phone");
    }
}
class Child extends Parent{
    mobile(){
        console.log("child phone number");
    }
}
var ch=new Child()
ch.mobile()