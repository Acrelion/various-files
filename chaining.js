function MyObj(name, value){
	this._name = name;
	this._value = value;
}

MyObj.prototype.increase = function(howMany) {
	this._value += howMany;
	return this;
};

MyObj.prototype.val = function(){
	console.log(this._value);
};