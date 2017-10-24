// /* Task Description */
// /*
//  * Create a module for a Telerik Academy course
//  * The course has a title and presentations
//  * Each presentation also has a title
//  * There is a homework for each presentation
//  * There is a set of students listed for the course
//  * Each student has firstname, lastname and an ID
//  * IDs must be unique integer numbers which are at least 1
//  * Each student can submit a homework for each presentation in the course
//  * Create method init
//  * Accepts a string - course title
//  * Accepts an array of strings - presentation titles
//  * Throws if there is an invalid title
//  * Titles do not start or end with spaces
//  * Titles do not have consecutive spaces
//  * Titles have at least one character
//  * Throws if there are no presentations
//  * Create method addStudent which lists a student for the course
//  * Accepts a string in the format 'Firstname Lastname'
//  * Throws if any of the names are not valid
//  * Names start with an upper case letter
//  * All other symbols in the name (if any) are lowercase letters
//  * Generates a unique student ID and returns it
//  * Create method getAllStudents that returns an array of students in the format:
//  * {firstname: 'string', lastname: 'string', id: StudentID}
//  * Create method submitHomework
//  * Accepts studentID and homeworkID
//  * homeworkID 1 is for the first presentation
//  * homeworkID 2 is for the second one
//  * ...
//  * Throws if any of the IDs are invalid
//  * Create method pushExamResults
//  * Accepts an array of items in the format {StudentID: ..., Score: ...}
//  * StudentIDs which are not listed get 0 points
//  * Throw if there is an invalid StudentID
//  * Throw if same StudentID is given more than once ( he tried to cheat (: )
//  * Throw if Score is not a number
//  * Create method getTopStudents which returns an array of the top 10 performing students
//  * Array must be sorted from best to worst
//  * If there are less than 10, return them all
//  * The final score that is used to calculate the top performing students is done as follows:
//  * 75% of the exam result
//  * 25% the submitted homework (count of submitted homeworks / count of all homeworks) for the course
//  */

function solve() {
	function checkTitle(title) {
		var twoSpacesRE = /\s\s+/g;

		if (typeof title !== "string") { // if its not a string, throw
			throw new Error("yes");
		 }

		if (title.length === 0 || title[0] === " " || title[title.length - 1] === " ") {
			throw new Error("yes"); // if it is empty string, it contains only spaces or starts, or ends with a space
		}
		if ( (title.match(twoSpacesRE)) ) { // if it has two spaces in it
			throw new Error("yes");
		}
	}

	function checkName(name) {
		var nameRE = /^[A-Z][a-z]*$/g;


		if (name === null || typeof name !== "string" || !(isNaN(name)) ) { // if the name is not a string, throw
			throw new Error("yes");
		 }
		if (name.length === 0 || name === " " ) {
			throw new Error("yes");              // if there are not letters at all
		}
		if (name[0] === " " || name[name.length - 1] === " ") { // if it starts or ends with a space
			throw new Error("yes");
		}
		if (name.split(" ").length > 2 || name.split(" ").length === 1 ) { // if there are three names given
			throw new Error("yes"); 									   // or its just one
		}
		// when we know we have somewhat good input, split the name and check for capitalization
		var spaceIndex = name.indexOf(" ");
		var firstname = name.substring(0,  spaceIndex);
		var lastname = name.substring(spaceIndex + 1);

		// if the capital letter is... not capitalized, throw
		if ( !(firstname.match(nameRE))  || !(lastname.match(nameRE))  ) {
			throw new Error("yes");
		}

		return [firstname, lastname];
	}
	


	var Course = {
		init: function(title, presentations) {
			// checks input for title, presentation titles, student names... START
				checkTitle(title);

				if (presentations.length === 0) { throw new Error("yes"); } //if no presentations are added
				if ( !(Array.isArray(presentations)) ) { throw new Error("yes"); }

				for (var i = 0; i < presentations.length; i++) { 		    // checks every presentation title
					checkTitle(presentations[i]);
				}
			// checks input for title, presentation titles, student names... END

				this.title = title;
				this.presentations = presentations;
				this.students = [];
				this.ids = [];
				this.hw = 0;
				
				return this;  // dangerous, but now we have an object (don't forget to return something in the init method)
		},
		addStudent: function(name) {
			var splittedNames = checkName(name); // in this way I don't have to separate them again
												 // this is like check + separate the names for me;
			var stud = {}; 						 // new empty student

			stud.firstname = splittedNames[0];
			stud.lastname = splittedNames[1];
			stud.id = this.students.length + 1;
			stud.homeworks = [];
			stud.score = 0;
			stud.performance = 0;

			this.students.push(stud);
			return stud.id;
		},
		getAllStudents: function() {
		    var formattedStudents = [];
			if (this.students.length === 0) {
				return formattedStudents;
			}

			for (var i = 0; i < this.students.length; i++) {
				var formatted = {};
				formatted.firstname = this.students[i].firstname;
				formatted.lastname = this.students[i].lastname;
				formatted.id = this.students[i].id;

				formattedStudents.push(formatted);
			}

			return formattedStudents;
			
		},
		submitHomework: function(studentID, homeworkID) {
			var indexOfStudent = 0;
			
			if ( isNaN(studentID) || isNaN(homeworkID) ) {
				throw new Error("yes");
			}
			if (studentID < 1 || studentID > this.students.length) {
				throw new Error("yes");
		    }
			if (homeworkID < 1 || homeworkID > this.presentations.length) {
				throw new Error("yes");
		    }
			
			for (var index = 0; index < this.students.length; index++) { //finds where in studen is the student with the given ID
				if (this.students[index].id === studentID) {
					indexOfStudent = this.students.indexOf( this.students[index] );
					break;
				}
		    }					
			this.students[indexOfStudent].homeworks.push(homeworkID);
			
			if (homeworkID > this.hw) {
				this.hw = homeworkID;
			}		
			
		},
		pushExamResults: function(results) {
			var alreadyHaveIds = [];
			
			for (var ind = 0; ind < results.length; ind++) {
				if (results[ind].StudentID < 1 || results[ind].StudentID > this.students.length) {
					throw new Error("yes");
				}
				if ( isNaN(results[ind].Score) ) { // if score is NaN, throw
					throw new Error("yes");
				}
				if (alreadyHaveIds.indexOf(results[ind].StudentID) > -1) { // if we found an ID we already used, throw
					throw new Error("yes");
				}
				
				alreadyHaveIds.push(results[ind].StudentID);
				
				// find the student with the given ID
				for (var sti = 0; sti < this.students.length; sti++) {
					if (this.students[sti].id === results[ind].StudentID) {
						this.students[sti].score = results[ind].Score;
						break;
					}
				}
				
			} // outer for loop for result
			
		},
		getTopStudents: function() {
			
			for (var idx = 0; idx < this.students.length; idx++) {
				// students final score is calculated as 75% of the final exam + 25% of count of submitted homeworks / count of all homeworks
				this.students[idx].performance = (0.75 * this.students[idx].score) + (0.25 * (this.students[idx].homeworks.length / this.hw) );				
			}
				
			
			this.students.sort(function (a, b) {
				return (a.performance === b.performance) ? 0 : (a.performance < b.performance) ? 1 : -1;
			});
			
			
			if (this.students.length <= 10) {
				return this.students.slice();
			}
			else {
				return this.students.slice(0, 11);
			}
		}
	};

	return Course;
}

var jsoop = solve();
//var jsoop = solve().init("JS OOP 2015", ["Title 1", "Title 2"]);
jsoop.init("Course Title", ["Title 1", "Title 2"]);
//console.log(jsoop.presentations);

jsoop.addStudent("Omicron Estea");
jsoop.addStudent("Mariana Kamenova");
jsoop.addStudent("One Two");


//jsoop.submitHomework(3, 1);
//jsoop.submitHomework(3, 2);
//jsoop.submitHomework(1, 1);
//jsoop.pushExamResults([{StudentID: 1, Score: 6}, {StudentID: 2, Score: 4}, {StudentID: 3, Score: 5}]);

console.log(jsoop.getAllStudents());
//console.log(jsoop.getTopStudents());

