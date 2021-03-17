let i=0;
while(i<10){
    console.log(i);
    i++
}

let i=10;
while(i<0){
    console.log(i);
    i--;
}

let i=0;
while(i<=50){
    if(i%2==0){
        console.log(`number ${i}is odd`);
    }
    else{
        console.log(`number ${i} is even`);
    }
}

for (let i=0;i<=10;i++){
    console.log(i);
}

//prime number//
var num=17;
var flag=0;

for(let i=2;i<number;i++){
    if (number%i==0){
        flag+=1;
    }
    else{
        flag=0;
    }
    if(flag==0){
        console.log("prime");
    }
    else{
        console.log("not prime");
    }
}
