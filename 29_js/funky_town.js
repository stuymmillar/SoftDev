/*
Scripters - Ricky Lin, Max Millar  
SoftDev1 pd06
K#29: Sequential Progression II: Electric Boogaloo... 
2018-12-20 R
*/


//list of random names
var studentList = ["ricky", "aaron", "kyle", "kaitlin", "tim", "bo", "damian", "michelle"];

var fib = function(args) {  
    
    //base cases
    if (args == 0) return 0;
    else if (args == 1) return 1;
    
    //recursive fib sequence
    else return fib(args - 1) + fib(args - 2);
}

var gcd = function(num, denom) {

    //find if one of the number is a GCD and return it if it is
    var temp = num % denom;
    if (temp == 0) return denom;
    
    //otherwise perform gcd again with the denom and the remainder
    else return gcd(denom, temp);
}


var randStudent = function() {

    //generate random number within range of the length of array
    var len = studentList.length;
    var rand = Math.floor(Math.random() * len);

    //return the string at the index
    return studentList[rand];
}

//creates function for printing 
var fibcall = function() {

    //random number to 20 
    var rand = Math.floor(Math.random() * 20)

    //get id of the paragraph and add the results to the HTML code
    var fibdisplay = document.getElementById("display")
    fibdisplay.innerHTML += "Fibb of " + rand + " is " + fib(rand) + "<br>";
    
    //log results
    console.log(fib(rand));
}

var gcdcall = function() {

    //random numbers 1 to 20 
    var randone = Math.floor(Math.random() * 19) + 1
    var randtwo = Math.floor(Math.random() * 19) + 1

    //console.log(randone);
    //console.log(randtwo);

    //get id of the paragraph and add the results to the HTML code
    var gcddisplay = document.getElementById("display")
    gcddisplay.innerHTML += "GCD of " + randone + " and " + randtwo + " is " + gcd(randone, randtwo) + "<br>";
    
    //log results
    console.log(gcd(randone, randtwo));
}

var randcall = function() {
    //save the random student's name
    var student = randStudent();

    //get id of the paragraph and add the results to the HTML code
    var randdisplay = document.getElementById("display")
    randdisplay.innerHTML += "The random student is " + student + "<br>";
    
    //log results
    console.log(student);
}

//get id of the buttons and listen for a click to call the functions
var fibbutton = document.getElementById("fibb");
fibbutton.addEventListener('click', fibcall);

var gcdbutton = document.getElementById("gcd");
gcdbutton.addEventListener('click', gcdcall);

var randbutton = document.getElementById("rand");
randbutton.addEventListener('click', randcall);


console.log("fib ------\n\n")
console.log("fib(1): " + fib(1));
console.log("fib(8): " + fib(8));
console.log("fib(4): " + fib(4));
console.log("gcd ------\n\n")
console.log("gcd(8, 10): " + gcd(8, 10));
console.log("gcd(10, 100): " + gcd(10, 100));
console.log("gcd(100, 10): " + gcd(100, 10));
console.log("randomStudent ------\n\n")
console.log(randStudent());
console.log(randStudent());
console.log(randStudent());
console.log(randStudent());
