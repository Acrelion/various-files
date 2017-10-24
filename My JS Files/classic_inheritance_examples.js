// parent
var Vehicle = (function(){
	
	function Vehicle(tires) {
		this.tires = tires;
		return this;
	}
	
	Vehicle.prototype.drive = function() {
		console.log("I am moving now!");
	};
	
	return Vehicle;
}());

// child
var Car = (function(){
	
	function Car(tires) {
		Vehicle.call(this, tires);
		return this;
		
	}
	
	Car.prototype = Object.create(Vehicle.prototype);
	Car.prototype.constructor = Car;
	
	Car.prototype.drive = function() {
		Vehicle.prototype.drive.call(this);
	}
	
	return Car;
}());


// testing
var vec = new Vehicle(2);
vec.drive();

var myCar = new Car(4);
myCar.drive();

console.log(vec instanceof Vehicle);
console.log(myCar instanceof Car);
console.log(myCar instanceof Vehicle);