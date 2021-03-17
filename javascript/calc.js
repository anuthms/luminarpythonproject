function displaybox(num){
    var res=document.querySelector('.res')
    res.value+=num
  
}
function answer(){
    var res=document.querySelector('.res').value
    var out=eval(res)
    document.querySelector('.res').value=out
}
function del(){
    var res=document.querySelector('.res').value;
    var data=res.slice(0,-1)
    document.querySelector('.res').value=data
}


