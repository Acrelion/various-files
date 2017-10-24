// A module is created. It can print a given message (string, num...)
// can repeat string given number of times. 

var customModule = (function() {

	function print(msg) {
		console.log(msg);
	}

	function repeat(str, num) {
		var result = "";
		for(var i = 0; i < num; i++) {  // can be done with return new Array(num + 1).join(str);
			result += str;
		}
		return result;
	}

	return {
		print: print,
		repeat: repeat,
	};
	
}()); // this is IIFE (Instantly initiated function expression. So its ready for work.

customModule.print("Hello!");
customModule.print("Wazaaaa!");



