// simple object constructor

var Person = (function () {
	
	function Person(name) {
		this.name = name;
	}
	
	Object.defineProperty(Person.prototype, "name", {
		get: function () {
			return this._name;
		},
		set: function (value) {
			if (typeof (value) === "string") {
				this._name = value;
				return this;
			}
			else {
				throw new Error("Invalid type input for name");
			}
		},
		enumerable: true
	});
	
	Person.prototype.introduce = function () {
		console.log("My name is: " + this.name);
	};
	
	return Person;

}());


var example = new Person("Petur");
console.log(example.name);