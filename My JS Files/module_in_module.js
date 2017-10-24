
// Here we don't have a real module - this is a clousure.
var namespace = (function () {
	
	var inner = (function () {
		return "Hello, I am inner";
	});	
	
	return inner;
});

//var first = namespace();   // we have to call them;
//console.log(first());



// now we have a module inside another module


var big = (function () {
	
	var smaller = (function () {
		return "I am the smaller one!";
	}());
	
	return smaller;
}());

//console.log(big);
                  // In this case the smaller is already invoked and when
				  // bigger returns it, it already have its content spewed out.
				  // In other words: we dont have to call the big or the smaller
				  // they are already called and ready.
				  // the same thing is done bellow but with two modules inside of a main one.
				  
				  
				  
// But what if we have two modules inside of one (every one is invoked on the spot);
// NOTE: The bad thing here is that we have all the sub modules invoked and consuming memory.
// NOTE 2: In this case we return the different sub modules as an object
        // and they are easily accessible.

var mainModule = (function () {
	
	var firstSub = (function (params) {
		return "I am firstSub!";
	}());
	
	var secondSub = (function () {
		return "I am but the secondSub, yo!";
	}());
	
	return {
		first: firstSub,
		second: secondSub
	};
	
}());

console.log(mainModule.first);