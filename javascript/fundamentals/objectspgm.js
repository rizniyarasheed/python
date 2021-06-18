//object is smilar method of dictionary[python]
//key values have no double quotes

var employee={
    id:1000,name:"rini",desig:"developer",salary:25000
}
console.log(employee["name"]);
//or
console.log(employee.name);

//checking for gender in there
console.log("gender" in employee);

//add gender in employee
employee["gender"]="male"
console.log(employee);

//iteration
for(let key in employee){
    console.log(key);
}