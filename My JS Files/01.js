// This program contains a function that accepts different number of parameters and
//prints their type.

/**Prints the type of the argument*/
function doSomething(arg) {
    var givenArgs = [].slice.apply(arguments);
    var givenArgsLen = givenArgs.length;

    if (givenArgsLen === 0) {
        console.log(typeof null);
	}
	else {
        givenArgs.forEach(function (element) {
            console.log(typeof element);
        });
	}
}

doSomething();

console.log("---------");

doSomething("Hello");

console.log("---------");

doSomething(1, true, null, "Hello", { hello: "Greetings" }, []);

