// We add a method to the String prototype which repeats a string given number of times.
// The same is done with Number where we are creating a method that gives us number to the power pow.

String.prototype.repeat = function (count) {
	count = count || 1; // guardian
    return (new Array(count + 1)).join(this);
};

// Adding new method to the Number object prototype 
// Every instance will have it.

Number.prototype.powten = function (pow) {
	pow = pow || 0; // guardian
	return Math.pow(this, pow);
	
};

// Here we are making something like a static method. We don't attach it to the prototype
// In other words, we attach this new method to the object string.

String.isBanana = function (str) {
	str = str || ""; // guardian
	return str === "banana";	
};



// Lets try them!
console.log("\nRepeating string 3 times:");
console.log("Hello ".repeat(3));

console.log("\n\nUsing the powten method of Number:");
var two = 2;
console.log(two.powten(10));

console.log("\n\nUsing now the 'static' method we attached to String:");
var myString = "orange";
console.log(String.isBanana(myString));

