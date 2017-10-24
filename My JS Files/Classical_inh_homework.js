/*
Classical Inheritance
   Task 1.

    Create a function constructor for Person. Each Person must have:
        properties firstname, lastname and age
            firstname and lastname must always be strings between 3 and 20 characters, containing only Latin letters
            age must always be a number in the range (0, 150), inclusive
                the setter of age can receive a convertible-to-number value
            if any of the above is not met, throw Error
        property fullname
            the getter returns a string in the format 'FIRST_NAME LAST_NAME'
            the setter receives a string is the format 'FIRST_NAME LAST_NAME'
                it must parse it and set firstname and lastname
        method introduce() that returns a string in the format 'Hello! My name is FULL_NAME and I am AGE-years-old'
        all methods and properties must be attached to the prototype of the Person
*/
	var Person = (function () {
		function isNameValid(name) {
			var re = /[^A-z]+/g;
			
			if (typeof (name) !== "string") { throw new Error("yes"); }
			
			// if (invalid chars are found - false || 	the length is too short or too long)
			if ( !!(name.match(re)) || !(name.length >= 3 && name.length <=20) ) {
				throw new Error("yes");
			}
			else {
				return true;
			}
		}
		
		function isAgeValid (age) {
			if (isNaN(age)) {
				throw new Error("yes");
			}
			
			if (+age < 0 || +age > 150) {
				throw new Error("yes");
			}
			
			return true;
		}
		
		function splitName(names) {
			names = names.replace(/\s\s+/g, ' '); // if we have multiple empty spaces	
			var index = names.indexOf(" ");
			
			if (index === -1) { throw new Error("yes"); }
			var first = names.substring(0, index);
			var second = names.substring(index + 1);
			
			if (isNameValid(first) && isNameValid(second)) {
				return [first, second];
			}
					
		}
		
		///The constructor takes firstname, lastname and age.
		function Person(firstname, lastname, age) {
			
			this.firstname = firstname;
			this.lastname = lastname;
			this.age = age;
		}
		
		// Adding getter and setter for the properties;
		Object.defineProperties(Person.prototype, {
			firstname: {
				get: function () {
					return this._firstname;
				},
				set: function (value) {
					if (isNameValid(value)) {
							this._firstname = value;
							return this;
					}
				}
			},
			lastname: {
				get: function () {
					return this._lastname;
				},
				set: function (value) {
					if (isNameValid(value)) {
							this._lastname = value;
							return this;
					}
				}
			},
			age: {
				get: function () {
					return this._age;
				},
				set: function (value) {
					if (isAgeValid(value)) {
						this._age = +value;
						return this;
					}
				}
				
			},
			fullname: {
				get: function () {
					return this._firstname + " " + this._lastname;
				},
				set: function (value) {
					var parsed = splitName(value);
					
					this._firstname = parsed[0];
					this._lastname = parsed[1];
					return this;
				}
			}	
		});
		
		// method introduce
		Person.prototype.introduce = function () {
			return "Hello! My name is " + this._firstname + " " + this._lastname + " and I am " + this._age + "-years-old";
		};
		
		return Person;
	}());






// Tests!

var gosho = new Person("Gosho", "Goshev", 300);
console.log(gosho.firstname, gosho.lastname, gosho.age);

gosho.firstname = "Pesho";
gosho.age = "20";
console.log(gosho.firstname, gosho.lastname, gosho.age);

gosho.lastname = "Peshov";
gosho.age = 10;
console.log(gosho.firstname, gosho.lastname, gosho.age);

console.log(gosho.fullname);
gosho.fullname = "Kiro Kirov";
console.log(gosho.fullname);
console.log(gosho.firstname);
gosho.firstname = "Plamen";
console.log(gosho.introduce());
console.log(gosho.hasOwnProperty("introduce"));
