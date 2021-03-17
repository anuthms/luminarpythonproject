var arr=[10,20,30,40,12,45,12,66,13,33]
//var square=arr.map(no=>no**2)
//console.log(square);

//arr.forEach(num=>console.log(square));
//arr.map((num)=>num**3).forEach(num=>console.log(num));
//arr.filter(num=>num%2==0).forEach(num=>console.log(num));
//arr.sort((no1,no2)=>no1-no2).forEach(num=>console.log(num));
//arr.sort((no1,no2)=>no1>no2?-1:1).forEach(num=>console.log(num));
let num=arr.reduce((num1,num2)=>num1+num2)
//console.log(num);
let min=arr.reduce((num1,num2)=>num1>num2?num2:num1)
console.log(min);






