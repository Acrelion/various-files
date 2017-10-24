// the parameter hi is kept inside name(), i.e. the function greeter is still in the memory.

function greeter(hi) {

	function name(name) {
		return hi + " " + name;
	}

	return name;
} 

var french = greeter("Bonjour");
console.log(french("Ivan"));
console.log(french("Omicron"));

