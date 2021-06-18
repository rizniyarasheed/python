//class = blue print,design pattern
//object = real world entity
//reference = operations

class Person{
   setPerson(age,name){
       this.age=age;
       this.name=name;
   }
   printPerson(){
       console.log(this.age+","+this.name);
   }
}

//object creation
//reference name=className()

var obj=new Person();
obj.setPerson(25,"nini")
obj.printPerson()