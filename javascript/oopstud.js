class Student{
     constructor(rol,course,name,marks){
        this.rol=rol;
        this.course=course;
        this.name=name;
        this.marks=marks;
    }
    printStudent(){
         console.log(this.name+ "," +this.marks+","+this.course+","+this.rol);
    }
}
var obj=new Student(001,"danjo","ajay",500);
obj.printStudent()