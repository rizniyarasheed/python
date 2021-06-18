//arrays
//insertion order preserved
//duplicates allowed
//indexing
//homogenious and hetrogenious data

// var data=[10,"hello",true,10.5];
// console.log(data);

//iteration
var numbers=[10,20,30,40,50]
// for(let i=0;i<numbers.length;i++){
//     console.log(numbers[i]);
// }

for(let number of numbers){
    console.log(number);
}

//add a number to array
//arrayname.push
//pop-->arrayname.pop
numbers.push(100)
console.log(numbers);

numbers.pop()
console.log(numbers);

//find eqal numbers in arrays
var arr1=[10,20,30,40]
var arr2=[21,22,30,31,40]

for(let i of arr1){
    for(let j of arr2){
        if(i==j){
            console.log(i);
        }
    }
}


//sorting

var arr3=[30,10,40,20,50,111]
arr3.sort()
console.log(arr3);

//advanced sorting using arrrow function
var arr3=[30,10,40,20,1005,50,111]
arr3.sort((no1,no2)=>no1-no2)//no1 must come before no2
console.log(arr3);
