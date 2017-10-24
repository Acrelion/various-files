var domElement = (function () {
	var domElement = {
		init: function (value) {
			this.name = value;
			return this;
		},
		hello : function () {
			return "Hello " + this.name;
		},
		introduction: function() {
			console.log("My name is " + this.name);
		}
	};
	
	return domElement;
}());

var obj = Object.create(domElement).init("Norian");
console.log(obj);

console.log(obj.name);
obj.introduction;
console.log(obj.hello());


