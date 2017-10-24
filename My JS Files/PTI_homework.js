/* Task Description */
/*
* Create an object domElement, that has the following properties and methods:
  * use prototypal inheritance, without function constructors
  * method init() that gets the domElement type
    * i.e. `Object.create(domElement).init('div')`
  * property type that is the type of the domElement
    * a valid type is any non-empty string that contains only Latin letters and digits
  * property innerHTML of type string
    * gets the domElement, parsed as valid HTML
	  * <type attr1="value1" attr2="value2" ...> .. content / children's.innerHTML .. </type>
  * property content of type string
    * sets the content of the element
    * works only if there are no children
  * property attributes
    * each attribute has name and value
    * a valid attribute has a non-empty string for a name that contains only Latin letters and digits or dashes (-)
  * property children
    * each child is a domElement or a string
  * property parent
    * parent is a domElement
  * method appendChild(domElement / string)
    * appends to the end of children list
  * method addAttribute(name, value)
    * throw Error if type is not valid
  * // method removeAttribute(attribute)
*/


/* Example
var meta = Object.create(domElement)
	.init('meta')
	.addAttribute('charset', 'utf-8');
var head = Object.create(domElement)
	.init('head')
	.appendChild(meta)
var div = Object.create(domElement)
	.init('div')
	.addAttribute('style', 'font-size: 42px');
div.content = 'Hello, world!';
var body = Object.create(domElement)
	.init('body')
	.appendChild(div)
	.addAttribute('id', 'cuki')
	.addAttribute('bgcolor', '#012345');
var root = Object.create(domElement)
	.init('html')
	.appendChild(head)
	.appendChild(body);
console.log(root.innerHTML);
Outputs:
<html><head><meta charset="utf-8"></meta></head><body bgcolor="#012345" id="cuki"><div style="font-size: 42px">Hello, world!</div></body></html>
*/


// ADD function solve() {    return domElement;}  around the task
//solve() {
var domElement = (function () {
	function isValid(val, RE) {
		 //a valid type is any non-empty string that contains only Latin letters and digits
		if (typeof (val) !== "string") { throw new Error("yes"); }
		if (val === "")  { throw new Error("yes"); }
		if ( !!(val.match(RE)) )  { throw new Error("yes"); }
	}
	
	function getAttr(obj) {
			 var attrToSort = [];
			 var sorted = [];
			 var result = "";	
			 	
			 for (var key in obj) {   					// extracts all the keys from obj
				 attrToSort.push(key);
			 }
			 
			 sorted = attrToSort.sort(); 				// sorts them
			 	 
			 for (var i = 0; i < sorted.length; i++) {	// for every key in sorted, add to result the matching pair
				 result += sorted[i] + "=\"" + obj[sorted[i]] + "\" ";
			 }	  
				  
			 return result !== "" ? " " + result.trim() : result; 
		 }
	
	function checkChild(child) {	//each child is a domElement or a string
		if (child === "") { throw new Error("yes"); }
		if ( !(domElement.isPrototypeOf(child)) ) {
			if (typeof (child) !== "string") {
				throw new Error("yes");  // if it is not both, throw error
			}			
		}
	}
	
	var domElement = {
		
		init: function(type) {
			isValid(type, /[^A-Za-z0-9]+/g);
			
			this.type = type;
			this.children = [];
			this.parent;
			this.content = "";
			this.innerHTML;
			this.atributes = {};
			return this;
			
						
		},
		appendChild: function(child) {
			checkChild(child);
			if (domElement.isPrototypeOf(child)) {
				child.parent = this;
			}
			
			this.children.push(child);
			return this;
		},
		addAttribute: function(name, value) {
			isValid(name, /[^A-Za-z0-9-]+/g);
			
			this.atributes[name] = value;
			return this;
		},
		removeAttribute: function (attribute) {
			isValid(attribute, /[^A-Za-z0-9-]+/g);
			if ( this.atributes.hasOwnProperty(attribute) ) {
				delete this.atributes[attribute];
				return this;
			}
			else { throw new Error("yes"); }
		},
		
     get innerHTML(){
		 //<type attr1="value1" attr2="value2" ...> .. content / children's.innerHTML .. </type>
		 var self = this;
		 
		 
		 	 
		 var result = "<" + self.type + getAttr(self.atributes) + ">"; // gets the first tag, i.e. <head>
		 
		 if (self.children.length === 0) { // if there are no children, get the content
			 result += self.content;
		 }
		 else {	 // if there are such: print their innerHTML instead
			 						  
		 	for (var i = 0; i < self.children.length; i++) {
				 
				 if (typeof self.children[i] === "string") {
					 result += self.children[i];
				 }
				 else {
					 result += self.children[i].innerHTML;
				 }
				 
		 	}
		 }
		 
		 result += "</" + self.type + ">"; // closing the tag
		 
		 return result.trim();
     }
	};
	
	return domElement;
} ());
//return domElement;    //UNCOMMENT WHEN PASTING TO BGCODER!
//}



/*
var meta = Object.create(domElement)
	.init('meta')
	.addAttribute('charset', 'utf-8');
var head = Object.create(domElement)
	.init('head')
	.appendChild(meta);
var div = Object.create(domElement)
	.init('div')
	.addAttribute('style', 'font-size: 42px');
div.content = 'Hello, world!';
var body = Object.create(domElement)
	.init('body')
	.appendChild(div)
	.addAttribute('id', 'cuki')
	.addAttribute('bgcolor', '#012345');
var root = Object.create(domElement)
	.init('html')
	.appendChild(head)
	.appendChild(body);
console.log(root.innerHTML);*/

			
			

