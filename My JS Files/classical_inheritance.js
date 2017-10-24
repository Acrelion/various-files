// Here we have two examples of IIFEs which in their nature are object prototypes.
// They are already invoked, but they contain constructors and can be called with new.
// If they are not already invoked, they don't work.

var Shape = ( function() {
	
	function Shape(x, y) { // it can be with diff name actually;
		this.x = x;
		this.y = y;
	}
	
	Object.defineProperty(Shape.prototype, "x", {
		get: function() {
			return this._x;
		},
		set: function(value) {
			this._x = value;
			return this;
		}
	});
	
	Object.defineProperty(Shape.prototype, "y", {
		get: function() {
			return this._y;
		},
		set: function(value) {
			this._y = value;
			return this;
		}
		
	});
	
	
	
	Shape.prototype.dimensions = function () {
		console.log("Dimensions are - x: " + this._x + " and y: " + this._y);
	};
	
	return Shape;
})();

///////////////////////////////////////// Child of  Shape;
var Rectangular = (function(parent){	
	
	
	function Rectangular(x, y, color) {
		parent.call(this, x, y);
		this.color = color;
		return this;
	}
	
	Rectangular.prototype = Object.create(parent.prototype);
	Rectangular.prototype.constructor = Rectangular;
	
	Object.defineProperty(Rectangular.prototype, "color",  {
		get: function() {
			return this._color;
		},
		set: function(value) {
			this._color = value;
			return this;
		}
	})
	
	
	Rectangular.prototype.dimensions = function() {
		parent.prototype.dimensions.call(this);
	}
	
	Rectangular.prototype.showColor = function() {
		console.log("My color is " + this._color);
	}
	
	return Rectangular;
}(Shape));




// testing
console.log(Shape);
var myShape = new Shape(5, 7);
console.log(myShape.x);

myShape.dimensions();


// testing Rectangular now
var myRec = new Rectangular(3, 10, "Green");
console.log(myRec.x + "  " + myRec.y);
myRec.dimensions();
myRec.showColor();

console.log(myRec instanceof Rectangular);
console.log(myRec instanceof Shape);


