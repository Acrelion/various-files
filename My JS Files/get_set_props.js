// Example of get/set for properties of an object.

function Person(name, age) {
	this.name = name; // bellow we change this property to have get/set method.
	this.age = age;
	// new property introduction is created bellow and it has only get method, i.e. it can be acessed only;
}
									    //NOTE: If it doesn't work, change name to _name
Object.defineProperty(Person.prototype, "name", { // here we use different name to show we do some internal bussiness (its simple)
	get: function () {
		return this._name;
	},
	set: function (value) {
		if (typeof (value) !== "string") {
			throw new Error("Invalid input!");
		}
		
		this._name = value;
		return this;
	},
	enumerable: true // in this way all the props will be shown in FOR IN LOOP (_name, age, name) - optional	
});

Object.defineProperty(Person.prototype, "age", {
	get: function () {
		return this._age;
	},
	set: function (value) {
		this._age = value;
		return this;
	}
});


Object.defineProperty(Person.prototype, "introduction",  { // adding new property which has only a get method
	get: function () {
		return "Hello, my name is " + this.name + " and I am " + this.age + " years old.";
	}
});






/// Testing now!
var p = new Person("John", 200);

console.log(p._name, p._age);

p.name = "Alexander"; // here we change the value for name, but we are actually using the get method for name
console.log(p.introduction);