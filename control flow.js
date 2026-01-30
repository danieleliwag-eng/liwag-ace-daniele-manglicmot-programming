 // condtional statement
// indentation always to refer the 
// if (condition1) {
  //  block of code to be executed if condition1 is true
// } else if (condition2) {
    //  block of code to be executed if the condition1 is false and condition2 is true
//   } else {
    //  block of code to be executed if the condition1 is false and condition2 is false
//   }
// meanning: Use if to specify a block of code to be executed, if a specified condition is true. Use else to specify a block of code to be executed, if the same condition is false. Use else if to specify a new condition to test, if the first condition is false.
// example
let num1 = 3;
let num2 = 4;
let num3 = 5;
let result = num1 > num2;
if(num1 > num2 && num1 > num3){
    console.log("num1 is greater")
}
else if( num1 > num2 && num2 ) {
    console.log("num2 is greater");
   console.log('yee');
}
console.log("byee......")

    
    

