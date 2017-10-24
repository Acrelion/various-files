// In this case the two programs do almost the same things (they have the same names) so
// they are splitted in two IIFEs. In the first one we have two functions which you dont even need to call
// they are already called. The problem is with getting the input. A form can be used or prompt if its connected
// with a HTML file.

var first = function () {
	var name = "Omicron";
	var family = "Estea";
	
	function calculate(a, b) {
		return a + b;
	}
	function print(fname) {
		
		console.log("Hello, %s! Nice to meet you!", fname);
	}
	
	function sayGoodbye(firstname, lastname) {
		console.log("Au revoir, %s %s.", firstname, lastname);
	}
	return {
		print: print(name),         // called here
		calculate: calculate, 		// you need to call it to use it
		goodbye: sayGoodbye(name, family) // called here too
	};
}();

var second = function () {
	function difference(a, b) {
		return a - b;
	}
	function print(msg) {
		console.log(msg);
	}
	return {
		difference: difference,    // you need to call it to use it
		print: print			   // you need to call it to use it
	};
}();



second.print("This is my custom message!");
second.print(first.calculate(5, 4)); // using the second's method print to print the first.calculate