// This is the second exam at telerik academy - 9.7.2015

function solve(){
        var ids = [];
        var catalogIDs = [];

        var check = {
                checkForEmptyString: function(value) {
                      value = value || "";

                      if (value === "") { throw new Error("yes"); }
                },
                checkName: function(value) {
                        value = value || "";

                        if (typeof value !== "string") { throw new Error("yes"); }
                        if (value.length < 2 || value.length > 40) { throw new Error("yes"); }
                },
                checkISBN: function(value) {
                        value = value || "";
                        var onlyDigitsRE = /[A-Za-z,.\s+!&#@$%*:"";<>')?/|\\=(-]+/g;

                        if (typeof value !== "string") { throw new Error("yes"); }
                        if ( value.length < 10 || value.length > 13 ) { throw new Error("yes"); }
                        if ( (value.match(onlyDigitsRE)) ) { throw new Error("yes"); }

                },
                checkGenre: function(value) {
                        value = value || "";

                        if (typeof value !== "string") { throw new Error("yes"); }
                        if ( value.length < 2 || value.length > 20 ) { throw new Error("yes"); }
                },
                checkDuration: function(value) {
                        value = value || 0;

                        if (value < 0)  { throw new Error("yes"); }
                },
                checkRating: function(value) {
                        value = value || 0;

                        if (value < 1 || value > 5) { throw new Error("yes"); }
                },
                checkItemsArray: function(arr) {


                        if (arr.length === 0) { throw new Error("yes"); }

                        for (var i = 0; i < arr.length; i++) {

                                if ( Object.getPrototypeOf(arr[i]) !== item) {
                                     throw new Error("yes");

                                }

                        }
                },
                checkItemsArray2: function(arr) {


                        if (arr.length === 0) { throw new Error("yes"); }

                        for (var i = 0; i < arr.length; i++) {

                                if ( Object.getPrototypeOf(arr[i]) !== book) {
                                     throw new Error("yes");

                                }

                        }
                },
                checkItemsArray3: function(arr) {


                        if (arr.length === 0) { throw new Error("yes"); }

                        for (var i = 0; i < arr.length; i++) {

                                if ( Object.getPrototypeOf(arr[i]) !== media) {
                                     throw new Error("yes");

                                }

                        }
                },

                checkId: function(id) {
                        if (typeof id !== "number") { throw new Error("yes"); }
                        if ( isNaN(id) || !( isFinite(id) ) ) { throw new Error("yes"); }
                },
                checkPattern: function(pattern) {
                        if (typeof pattern !== "string") { throw new Error("yes"); }
                        if (pattern.length < 1) { throw new Error("yes"); }
                },

                checkTop: function(top) {
                        top = top || "";

                        if (typeof top !== "number") {
                             throw new Error("yes");
                        }
                        if (top < 1) { throw new Error("yes"); }
                }
        };

	/////////////////////////////////
        var item = {
                init: function(name, description) {
                        check.checkName(name);
                        check.checkForEmptyString(description);

                        this.id = ids.length + 1;
                        ids.push(this.id);

                        this.name = name;
                        this.description = description;

                        return this;
                }
        };

        var book = {
                init: function(name, isbn, genre, description) {
                        check.checkISBN(isbn);
                        check.checkGenre(genre);

                        item.init.call(this, name, description);

                        this.isbn = isbn;
                        this.genre = genre;

                        return this;
                }
        };


        var media = {
                init: function(name, rating, duration, description) {
                        check.checkDuration(duration);
                        check.checkRating(rating);

                        item.init.call(this, name, description);

                        this.rating = rating;
                        this.duration = duration;

                        return this;
                }
        };

        var catalog = {
                init: function(name) {
                       check.checkName(name);

                       this.id = catalogIDs.length + 1;
                       catalogIDs.push(this.id);

                       this.name = name;

                       this.items = [];

                       return this;

                }

        };

        Object.defineProperty(catalog, "search", {
               value: function(pattern) {
                       check.checkPattern(pattern);

                        var result = [];
                        pattern = pattern.toLowerCase();

                        for (var y = 0; y < this.items.length; y++) {

                             if (this.items[y].name.toLowerCase().indexOf(pattern) > -1) {
                                     result.push(this.items[y]);
                                     
                             }
                             else if ( this.items[y].description.toLowerCase().indexOf(pattern) > - 1 ) {
                                     result.push(this.items[y]);
                                     
                             }

                        }

                        return result;
                }
        });

        Object.defineProperty(catalog, "add", {
                value: function(parameter) {


                        if (typeof parameter === "undefined") { throw new Error("yes"); }

                        var converted = [].slice.apply(arguments);
                        check.checkItemsArray(converted);


                        this.items = this.items.concat(converted);
                        return this;

                }
        });

        Object.defineProperty(catalog, "find", {
                value: function(param) {

                        if (typeof param === "number") {
                                check.checkId(param);

                                for (var j = 0; j < this.items.length; j++) {
                                        if ( this.items[j].id === param ) {
                                                return this.items[j];
                                        }
                                }
                        } // end of if 1

                        if (typeof param === "object") {
                                var result = [];

                                // looping trough all the items we have in the catalog
                                for (var k = 0; k < this.items.length; k++) {

                                     // for every property in param, check if we have a match between
                                     // the item and the option
                                     for (var key in param) {

                                             // if they have such keys, compare their key's values
                                             if (param.hasOwnProperty(key) &&  this.items[k].hawOwnProperty(key)) {

                                                    if ( this.items[k][key] === param[key] ) {
                                                            result.push(this.items[k]);
                                                            break;
                                                    }
                                             }

                                     }

                                }
                                return result;
                        } // end of if 2

                }
        });

        var bookCatalog = {
               init: function (name) {
                       catalog.init.call(this, name);

                       return this;
               },

               add: function(parameter) {
                       if (typeof parameter === "undefined") { throw new Error("yes"); }

                        var converted = [].slice.apply(arguments);
                        check.checkItemsArray2(converted);


                        this.items = this.items.concat(converted);
                        return this;
               },

               getGenres: function() {
                       var genres = []
                       var uniqueGenres = [];

                       for (var v = 0; v < this.items.length; v++) {

                            

                               genres.push(this.items[v]["genre"]);

                            

                       } // end of for loop

                     // filtering the repeating elements;
                     uniqueGenres = genres.filter(function(item, pos) {
                             return genres.indexOf(item) === pos;
                     })
                     
                     var fun = [];
                     
                     for (var jj = 0; jj < uniqueGenres.length; jj++) {
                            fun.push(uniqueGenres[jj].toLowerCase());
                             
                     }

                     return fun;
               },

               find: function(param) {

                        if (typeof param === "number") {
                                check.checkId(param);

                                for (var j = 0; j < this.items.length; j++) {
                                        if ( this.items[j].id === param ) {
                                                return this.items[j];
                                        }
                                }
                                return [];
                        } // end of if 1

                        if (typeof param === "object") {
                                var result = [];

                                // looping trough all the items we have in the catalog
                                for (var k = 0; k < this.items.length; k++) {
                                     
                                     if (param.hasOwnProperty("id") ) {
                                             
                                             if (this.items[k]["id"] === param["id"] ) {
                                                     result.push(this.items[k]);
                                                            continue;
                                             }
                                     }
                                     
                                     else if (param.hasOwnProperty("name") ) {
                                             
                                             if (this.items[k]["name"] === param["name"] ) {
                                                     result.push(this.items[k]);
                                                            continue;
                                             }
                                     }
                                     
                                     else if (param.hasOwnProperty("genre") ) {
                                             
                                             if (this.items[k]["genre"] === param["genre"] ) {
                                                     result.push(this.items[k]);
                                                            continue;
                                             }
                                     }
                            

                                } // end of loop
                                
                                return result;
                        } // end of if 2

                }
        };

        Object.defineProperty(bookCatalog, "search", {
               value: function(pattern) {
                       check.checkPattern(pattern);

                        var result = [];
                        pattern = pattern.toLowerCase();

                        for (var y = 0; y < this.items.length; y++) {

                             if (this.items[y].name.toLowerCase().indexOf(pattern) > -1) {
                                     result.push(this.items[y]);
                                     continue;
                             }
                             else if ( this.items[y].description.toLowerCase().indexOf(pattern) > - 1 ) {
                                     result.push(this.items[y]);
                                     continue;
                             }

                        }

                        return result;
                }
        });

        var mediaCatalog = {
               init: function (name) {
                       catalog.init.call(this, name);

                       return this;
               },
               add: function(parameter) {
                       if (typeof parameter === "undefined") { throw new Error("yes"); }

                        var converted = [].slice.apply(arguments);
                        check.checkItemsArray3(converted);


                        this.items = this.items.concat(converted);
                        return this;
               },

               getTop: function(count) {
                       check.checkTop(count);

                       var result = [];
                       var sorted;

                       function compareMovies(a, b) {
                               if (a.rating < b.rating) {return -1 }
                               if (a.rating > b.rating) { return 1}
                               return 0;
                       }

                       sorted = this.items.sort(compareMovies);

                       for (var i = 0; i < count; i++) {
                               result.push( {id: sorted[i].id,  name: sorted[i].name} )

                       }

                       return result;
               },

               getSortedByDuration: function() {
                    //The media must sorted by: descending by duration
                    //                          ascending by id

                    function sortByDurationAndId(duration, id) {
                           return function (a, b) {
                                   if (a.duration > b.duration) {
                                           return -1;
                                   }
                                   else if (a.duration < b.duration) {
                                           return 1;
                                   }

                                   if (a.id < b.id) {
                                           return -1;
                                   }
                                   else if (a.id > b.id) {
                                           return 1;
                                   }

                                   else {
                                           return 0;
                                   }
                           }
                    }

                    return this.items.sort(sortByDurationAndId(this.duration, this.id));

               }
        };


	return {
            	getBook: function (name, isbn, genre, description) {
                        //return a book instance
        		return Object.create(book).init(name, isbn, genre, description);
                },
                getMedia: function (name, rating, duration, description) {
                        //return a media instance
                        return Object.create(media).init(name, rating, duration, description);
                },
                getBookCatalog: function (name) {
                        //return a book catalog instance
                        return Object.create(bookCatalog).init(name);
                },
                getMediaCatalog: function (name) {
                        //return a media catalog instance
                        return Object.create(mediaCatalog).init(name);
                }
	};


}


// sample usage
var module = solve();
var catalog = module.getBookCatalog('John\'s catalog');

var book1 = module.getBook('The secrets of the JavaScript Ninja', '1234567890', 'IT', 'A book about JavaScript');
var book2 = module.getBook('JavaScript: The Good Parts', '0123456789', 'IT', 'A good book about JS');


catalog.add(book1);
catalog.add(book2);

var media = module.getMediaCatalog("Hello Media!");
//var movie = module.getMedia("name")

//console.log(media);
console.log(catalog.getGenres());

//console.log(catalog.find(book1.id));
//returns book1

//console.log(catalog.find({id: book2.id, genre: 'IT'}));
//returns book2

//console.log(catalog.search('js'));
// returns book2

//console.log(catalog.search('javascript'));
//returns book1 and book2


//console.log(catalog.search('Te sa zeleni'))
//returns []
