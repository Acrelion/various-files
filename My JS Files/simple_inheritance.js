// Simple Inheritance between two object prototypes.
	// We have the parent prototype Person and Studen who inherits Person's properties
	// by calling to the Person's prototype to get them and adds another property grade.


function Person (name, age) {
	this.name = name;
	this.age = age;
}

// adding a method to the parent Person
Person.prototype.introduction = function () {
	console.log("My name is " + this.name);
};


function Student (name, age, grade) {
	Person.call(this, name, age);
	this.grade = grade;
}

Student.prototype = new Person(); // Setting the Student's prototype to an instance of the parent;
								  // i.e. it becomes the same function or something like that.


// Let's check!

var example = new Student("Tectonic", 20, 6);
console.log(example.name);
console.log(example.age);
console.log(example.grade);

// Using the parent's method on the child Student;
// Why this works? Because we already have set the Student's prototype to an instance of the parent;
example.introduction();

// additional checks
console.log(example instanceof Student);
console.log(example instanceof Person); // Here we have also true, because we said that the prototype
									    // of Student is an instance of Person. (ln 16);
