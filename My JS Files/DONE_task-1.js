/* Task Description */
/* 
	*	Create a module for working with books
		*	The module must provide the following functionalities:
			*	Add a new book to category
				*	Each book has unique title, author and ISBN
				*	It must return the newly created book with assigned ID
				*	If the category is missing, it must be automatically created
			*	List all books
				*	Books are sorted by ID
				*	This can be done by author, by category or all
			*	List all categories
				*	Categories are sorted by ID
		*	Each book/catagory has a unique identifier (ID) that is a number greater than or equal to 1
			*	When adding a book/category, the ID is generated automatically
		*	Add validation everywhere, where possible
			*	Book title and category name must be between 2 and 100 characters, including letters, digits and special characters ('!', ',', '.', etc)
			*	Author is any non-empty string
			*	Unique params are Book title and Book ISBN
			*	Book ISBN is an unique code that contains either 10 or 13 digits
			*	If something is not valid - throw Error
*/
function solve() {
	var library = (function () {
		var books = [];
		var categories = [];
		
		function listBooks(obj) {
			
			if (obj) {
				
				if (obj.hasOwnProperty("category")) { // if category is provided
				var booksWithCategory = [];
				
				for (var i = 0; i < books.length; i++) {
					if (books[i].category === obj.category) { booksWithCategory.push(books[i]); }
				}
				
				return booksWithCategory;
				}
				else if (obj.hasOwnProperty("author")) { // if author is provided
					var booksWithAuthor = [];
					
					for (var i = 0; i < books.length; i++) {
					if (books[i].author === obj.author) { booksWithAuthor.push(books[i]); }
				}
				
				return booksWithAuthor.sort(function (a, b) {return a.ID - b.ID; });
				}
			}
			
			else {
				return books;
			}
			
			
		}
		
		function addBook(bookToAdd) {
			var book = {};
			var cat = {};
			
					
			if ( //1. something is undefined, throw error
				bookToAdd.title === undefined && 
				bookToAdd.isbn === undefined &&
				bookToAdd.author === undefined &&
				bookToAdd.category === undefined
				) {
					throw new Error("yes");
				}
			
			//2. check if the length is valid
			if (bookToAdd.title.length < 2 || bookToAdd.title.length > 100) { 
				throw new Error("yes");
			}
			
			//3. check if category length is valid
			if (bookToAdd.category !== undefined && (bookToAdd.category.length < 2 || bookToAdd.category.length > 100)) { 
				throw new Error("yes");
			}
			
			//4. check if the title is unique (the function returns true or false)
			// this is done by looking over the entire array of books
			if ( (function checkForValid() {							  
				for (var i = 0; i < books.length; i++) {		  
					if (books[i].title === bookToAdd.title) return true;
				}
				return false;
			}()) )
			{		
		    	throw new Error("yes");
			}

			//5. check if the author parameter is valid	(if its empty, return error)		
			if (bookToAdd.author === "") {
				throw new Error("yes");
			}
			 
			//6. check if the ISBN is unique (the function returns true or false)
			// this is done by looking over the entire array of books
			if ( (function checkForValid() {							  
				for (var i = 0; i < books.length; i++) {		  
					if (books[i]["isbn"] === bookToAdd.isbn) return true;
				}
				return false;	
			}()) 
			){	
				throw new Error("yes");
			}
			
			//7. check if isbn length is either 10 or 13
			if (bookToAdd.isbn.toString().length !== 10 && bookToAdd.isbn.toString().length !== 13) {
				throw new Error("yes");
			}
			
			//8. check if isbn contains something that is not a digit
			if (isNaN(bookToAdd.isbn)) {
				throw new Error("yes");
			}
			
			// if everything is ok, fill the object up;
			book.ID = books.length + 1; 
			book.title = bookToAdd.title;
			book.isbn = bookToAdd.isbn;
			book.author = bookToAdd.author;
			book.category = bookToAdd.category || "";
			
			if (!(function checkIfAnyExists() {	// if a category doesnt exist, add one						  
				for (var i = 0; i < categories.length; i++) {				  
					if (categories[i]["name"] === bookToAdd.category && categories.length > 0) return true;
				}
				return false;	
			}())
			) 
			{
				cat.name = bookToAdd.category;
				cat.ID = categories.length + 1;
				categories.push(cat);
			}
			
			books.push(book);
			return book;
		}

		function listCategories() {
			var categoriesArr = [];
			
			categories.sort( function(a, b) { return a.ID - b.ID; } );
			
			for (var kk = 0; kk < categories.length; kk++) {
				categoriesArr.push(categories[kk]["name"]);
			}
								
			return categoriesArr;
		}

		return {
			books: {
				list: listBooks,
				add: addBook
			},
			categories: {
				list: listCategories
			}
		};
	} ());
	
	
	return library;
}

/*
// initiate the module
var example = solve();

// add a new book
example.books.add( { title:"Eon", isbn: 1234567890, author: "Grizlly Bear", category: "Yes" });
example.books.add( { title:"Elantris", isbn: 1010102233, author: "Branden Sanders", category: "No" });
example.books.add( { title:"Eternity", isbn: 5554443331, author: "Grizlly Bear", category: "Yes" });
//console.log(example.books.list());
console.log(example.books.list({ author: "Grizlly Bear" }));


// list the books we have
//console.log("-----------------------");
console.log(example.categories.list());
*/