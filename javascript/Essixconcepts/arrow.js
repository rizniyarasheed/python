//var add=(num1,num2)=>num1-num2

//var sub=(num1,num2)=>num1+num2
//console.log(sub(20,10));

//var cube=num1=>num2**3;


//MAP()


var arr=[10,20,30,40]
//squares
var squares=arr.map(no=>no**2)
console.log(squares)//[ 100, 400, 900, 1600 ]
arr.forEach(num=>console.log(num))//10 20 30 40

arr.map(no=>no**2).forEach((num=>console.log(num)))

//cube
arr.map((num)=>num**3).forEach((num=>console.log(num)))


//FILTER()

//find even numbers
var arr1=[11,13,12,16,14,15]
arr1.filter(num=>num%2==0).forEach(num=>console.log(num))

//SORTING
arr.sort((no1,no2)=>no1-no2).forEach(num=>console.log(num))
//another method
arr1.sort((no1,no2)=>no1>no2?-1:1).forEach(num=>console.log(num))


//REDUCE()
//FIND SUM OF ARRAY
let sum=arr.reduce((num1,num2)=>num1+num2)
console.log(sum);

//min of array2
let min=arr1.reduce((num1,num2)=>num1>num2?num2:num1)
console.log(min);

//max
let max=arr1.reduce((num1,num2)=>num1>num2?num1:num2)
console.log(max);

