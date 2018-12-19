//Team Gooble - Max Millar and Stefan Tan
//SoftDev1 pd06
//K28 -- Sequential Progression
//2018-12-18

var fibonnaci = function(n) {
    if (n == 0){
	return 0;
    }
    if (n == 1){
	return 1;
    }
    return (fibonnaci(n - 1) + fibonnaci(n - 2));
};

var gcd = function(a, b){
    if (b == 0){
	return a;
    }
    temp = a
    a = b
    b = temp % b
    return gcd(a, b);
};

var students = ["Bob", "Steve", "Kevin", "Tim", "Wally", "Tom", "Jane"];

var randomStudent = function() {
    rand = Math.floor(Math.random()*students.length);
    return students[rand];
};
