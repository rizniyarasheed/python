class Employee{
    constructor(eid,name,sal,desig){
        this.eid=eid;
        this.name=name;
        this.sal=sal;
        this.desig=desig;

    }
    printDeatils=()=>{
       console.log(this.eid+this.name+this.sal+this.desig);
    }
}

var employee=[]
var obj=new Employee(100,"anu",25000,"developer")
var obj1=new Employee(101,"arun",22000,"developer")
var obj2=new Employee(102,"ravi",23000,"qa")
var obj3=new Employee(103,"ram",27000,"qa")
employee.push(obj)
employee.push(obj1)
employee.push(obj2)
employee.push(obj3)


//print all designation
employee.forEach(emp=>console.log(emp.desig))

//add 2000 bonous in salary
//employee.map(emp=>emp.sal+2000).forEach(sal=>console.log(sal))

//convert employee name into uppercase
employee.map(emp=>emp.name.toUpperCase()).forEach(name=>console.log(name))

//print employee details whos desig="developer"
//employee.filter(emp=>emp.desig="developer").forEach(emp=>console.log(emp))

//sort employee salary highest to lowest
employee.sort((o1,o2)=>o1.sal>o2.sal?-1:1).forEach(emp=>console.log(emp))

//highest salaray in employee using reduce fun
const sal=employee.map(obj=>obj.sal).reduce((sal1,sal2)=>sal1>sal2?sal1:sal2)
console.log(sal);