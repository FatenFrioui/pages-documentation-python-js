//control flow if-- else if-- else
//conditional ternary operator
let thename="Sou";
let thegender="Male"
let theage=40;

if(thegender==="Male"){
    console.log("Mr")
} else{
    console.log("Mrs") 
}
//condition ? if true : if false
thegender==="Male" ? console.log("Mr") : console.log("Mrs");
let result= thegender==="Male" ? "Mr" : "Mrs";
document.write(result);
console.log(thegender==="Male" ? "Mr" : "Mrs") ;

console.log(`Hello ${thegender==="Male" ? "Mr" : "Mrs"} ${thename}`) ;

theage<20 ? console.log(20)
: theage>20 && theage<60 ? console.log("20 to 60")
: theage>60 ? console.log("larger than 60")
: console.log("unknown")
// changer null, 0 et undefined
let price=100;
// let price=0;
// let price=null;
// let price="";
console.log(`the price is ${price || "free"}`);
console.log(`the price is ${price ?? "free"}`); //pour null c tout