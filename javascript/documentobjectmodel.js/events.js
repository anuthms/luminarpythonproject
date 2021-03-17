var clk=document.querySelector("#clk")

clk.addEventListener('click',()=>{
    clk.textContent="clicked";
    clk.style.color="red";
})

var dbl=document.querySelector("#dbl")

dbl.addEventListener('dblclick',()=>{
    dbl.textContent="doubleclicked";
    dbl.style.color="green";
})

var ove=document.querySelector("#ove")

ove.addEventListener("mouseout",()=>{
    ove.textContent="mouse not over me";
    ove.style.color="yellow";
})