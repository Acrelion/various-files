// A module is created where it finds and puts into two new arrays
// the odds and even numbers.

var result = function findOddsAndEvens (arr) {
	var evens = [];
	var odds = [];

	arr.forEach(function(element) {
		if (element % 2 === 0) evens.push(element);
		else odds.push(element);
	});

	return {
		evens: evens,
		odds: odds
	};
};

// here we are using the initial result module
var arrr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];

console.log(result(arrr).evens);
console.log(result(arrr).odds);




// a new example with creating new variable by using new array and reusing the module
var arrr2 = [4, 5, 7, 6];

var newResult = result(arrr2);
console.log(newResult.evens);
