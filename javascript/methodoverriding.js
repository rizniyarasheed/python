//different class same method

class Parent{
    phone(){
        console.log("parent phone");
    }
}
class Child extends Parent{
    phone(){
        console.log("child phone method");
    }
}

var ch=new Child()
ch.phone()
