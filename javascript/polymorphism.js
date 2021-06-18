//many forms
//method overloading==many forms different number of arguments
//method overriding

//method overloading eg:
class Calc{
    add(){
        console.log("onside no arg method");
    }
    add(num){
        console.log("inside one arg");
    }
    add(num1,num2){
        console.log("inside two arg ");
    }
}

var Cal=new  Calc()
Cal.add(10,20);
Cal.add(10);
