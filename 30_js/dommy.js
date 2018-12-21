//Team Gooble - Max Millar and Stefan Tan
//SoftDev1 pd06
//K30 -- Sequential Progression III: Season of the Witch
//2018-12-20

var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e["target"]["innerHTML"];
    //console.log(e["target"]["innerHTML"]);
};

var revertHeading = function() {
  var h = document.getElementById("h");
  h.innerHTML = "Hello World!";
}

var removeItem = function(e) {
    var item = e.target;
    item.parentNode.removeChild(item);
    //console.log(item);
};

var lis = document.getElementsByTagName("li");

for (var i=0; i<lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', revertHeading);
    lis[i].addEventListener('click', removeItem);
    //console.log(lis[i]);
};

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', revertHeading);
    item.addEventListener('click', removeItem);
    list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(args) {
    //base cases
    if (args == 0) return 0;
    else if (args == 1) return 1;
    //recursive fib sequence
    else return fib(args - 1) + fib(args - 2);
}

var fibcount = 0;

var addFib = function(e) {
    //console.log(e);
    var list = document.getElementById("fiblist");
    var item = document.createElement("li");
    item.innerHTML = fib(fibcount);
    fibcount++;
    list.appendChild(item);
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
