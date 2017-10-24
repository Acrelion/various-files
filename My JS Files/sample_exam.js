/*
JavaScript OOP 2015 - Audio Player

    Create an object that enables creation of playlists and audio players
    Each playlist has the following properties and methods:
        A property name
        A property audios
        A method addAudio(audio)
            Adds a audio to the player
            The same audio can be added multiple times
            Each audio has a name and an id
                If the audio is firstly added to any playlist, an ID is generated for it
                If the audio is previosly added to any playlist, its ID is reused
            Enables chaining
        A method getAudioById(id)
            Returns the audio that has the provided ID
            Returns null, if no audio is found with the provided ID
        A method removeAudioById(id)
            Removes the leftmost occurence of the audio with the provided ID
            Enables chaining
*/

function solve() {
    var ids = []
    
    function checkLength(arg) {
        if (typeof arg !== "string") {
            throw new Error("yes");
        }
        if (arg.length < 3 || arg.length > 25) {
            throw new Error("yes");
        }
    }
    
    var player = {
        
        init: function(name) {  
            checkLength(name);
                     
            this.name = name;
            this.id = ids.length + 1;
            this.playlists = [];
            
            ids.push(this.id);
            
            return this;
        },
        
        addPlaylist: function(playlistToAdd) {
            //Adds a playlist to the player
            if (Object.getPrototypeOf(playlistToAdd) !== playlist) {
                throw new Error("yes");
            }
            
            this.playlists.push(playlistToAdd);
            return this;
        },
        getPlaylistById: function(id) {
            //Finds and returns a playlist from the playlists in this player instance
            for (var index = 0; index < this.playlists.length; index++) {
                if (this.playlists[index].id === id) {
                    return this.playlists[index];
                }
                
            }
            return null;
        },
        removePlaylist: function(argument) {
            var index = -1;
            var id = 0;
            
            if (typeof argument === "number") { 
                 id = argument;
            }
            if (Object.getPrototypeOf(argument) === playlist) {
                 id = argument.id;
            }
            
                              
             for (var ii = 0; ii < this.playlists.length; ii++) {
                 if (this.playlists[ii].id === id) {
                        index = ii;
                        break;
                 }    
             }
                
             // after we found the index of the playlist with that id, remove it.   
             // if the index is still -1, then... we didn't found anything.
             if (index === -1) {
                 throw new Error("yes");
             }
             else {
                 this.playlists.splice(index, 1);
             }   
              
             return this;
        },
        
        listPlaylists: function(page, size) {
            if ( (page * size) > this.playlists.length  ) {
                throw new Error("yes");
            }
            if (page < 0 || size <= 0 ) {
                throw new Error("yes");
            }
            
            //TODO: Sort by name, then by ID the playlists.................................................
            
            if ( this.playlists.length < size ) {
                return this.playlists.slice();
            }
            else {// page * size = 20;    (page * size) + (size - 1) = 20 + 9 = 29;
                return this.playlists.slice( (page * size), ( (page * size) + size )  );
            }
        },
        
        contains: function(playable, playlist) {
            var itContains = false;
            
            // for every playlist in the playlists array
            for (var k = 0; k < this.playlists.length; k++) {
                
                //if we find a playlist with the same id we need
                if ( this.playlists[k].id = playlist.id) {
                    
                    // for every playable in this playlist
                    for (var q = 0; q < this.playlists[k].playables.length; q++) {
                        
                        // if we find a playable with the id of playable (the arg), then return true;
                        if (this.playlists[k].playables[q].id = playable.id ) {
                            itContains = true;
                            break;
                        }
                    }
                }
                
            }
            return itContains;
        },
        
        search: function(pattern) {
            var result = [];
            
            // for every playlist in this player playlists
            for (var idx = 0; idx < this.playlists.length; idx++) {
                
                // for every playable in the current playlist
                for (var z = 0; z < this.playlists[idx].playables.length; z++) {
                    
                    // if we find that it contains a playable with title that matches the pattern
                    if (  !!(this.playlists[idx].playables[z].title.match(pattern)) ) {
                        var tempObj = {};
                        tempObj.name = this.playlists[idx].name;
                        tempObj.id = this.playlists[idx].id;
                        
                        // add custom image of this object to an array;
                        result.push(tempObj);
                    }
                } 
                
            }
            
            return result;
        }       
        
        
    };
    
    var playlist = {
        init: function(name) {
            checkLength(name);
            
            this.name = name;
            this.id = ids.length + 1;
            this.playables = [];
            
            ids.push(this.id);
            
            return this;
        },
        
        addPlayable: function(playableVal) {
            
            this.playables.push(playableVal);
            return this;
        },
        
        getPlayableById: function(id) {
            //Returns the playable that has the provided id
            for (var index = 0; index < this.playables.length; index++) {
                if (this.playables[index].id === id) {
                    return this.playables[index];
                }
                
            }
            return null;
        },
        removePlayable: function(argument) {
            var index = -1;
            var id = 0;
            
            // if the given argument is a string, go over all the playables and search for 
            // one with such a name;
            if (typeof argument === "string") {
                for (var jk = 0; jk < this.playables.length; jk++) {
                    if (this.playables[jk].title === argument) {
                        id = this.playables[jk];
                        break;
                    }
                }
            }
            
            if (typeof argument === "number") { 
                 id = argument;
            }
            if (Object.getPrototypeOf(argument) === playable) {
                 id = argument.id;
            }
            
                              
             for (var ii = 0; ii < this.playables.length; ii++) {
                 if (this.playables[ii].id === id) {
                        index = ii;
                        break;
                 }    
             }
                
             // after we found the index of the playlist with that id, remove it.   
             // if the index is still -1, then... we didn't found anything.
             if (index === -1) {
                 throw new Error("yes");
             }
             else {
                 this.playables.splice(index, 1);
             }    
        },
        
        listPlayables: function(page, size) {
            if ( (page * size) > this.playables.length  ) {
                throw new Error("yes");
            }
            if (page < 0 || size <= 0 ) {
                throw new Error("yes");
            }
            
            //TODO: Sort by name, then by ID the playlists.................................................
            
            if ( this.playables.length < size ) {
                return this.playables.slice();
            }
            else {// page * size = 20;    (page * size) + (size - 1) = 20 + 9 = 29;
                return this.playables.slice( (page * size), ( (page * size) + size) );
            }
        }
        
    };
    
    var playable = {
        init: function(title, author) {
            checkLength(title);
            checkLength(author);
            
            this.id = ids.length + 1;
            this.title = title;
            this.author = author;
            
            ids.push(this.id);
            
            return this;  
        },
        
        play: function() {
            return this.id + ". " + this.title + " - " + this.author;
        }
        
    };
    
    var audio = {
        init: function(title, author, length) {
            
            if (typeof length !== "number" || length < 1) {
                throw new Error("yes");
            }
            
            playable.init.call(this, title, author);
            this.length = length;
            
            return this;
        },
        
        
        play: function() {
            var baseResult = playable.play.call(this);
            return baseResult + " - " + this.length;
        }
        
    };
    
    var video = {
        init: function(title, author, imdbRating) {
            
            if (typeof imdbRating !== "number") {
                throw new Error("yes");
            }
            if (imdbRating < 1 || imdbRating > 5) {
                throw new Error("yes");
            }
            
            playable.init.call(this, title, author);
            this.imdbRating = imdbRating;
            
            return this;
        },
        
        play: function() {
            var baseResult = playable.play.call(this);
            return baseResult + " - " + this.imbdRating;
        }
    };
    

    var module = {
        getPlayer: function (name){
            // returns a new player instance with the provided name
            return Object.create(player).init(name);
        },
        getPlaylist: function(name){
            //returns a new playlist instance with the provided name
            return Object.create(playlist).init(name);
        },
        getAudio: function(title, author, length){
            //returns a new audio instance with the provided title, author and length
            return Object.create(audio).init(title, author, length);
        },
        getVideo: function(title, author, imdbRating){
            //returns a new video instance with the provided title, author and imdbRating
            return Object.create(video).init(title, author, imdbRating);
        }
    };

    return module;
}




var result = solve();

//var player = result.getPlayer("Some name").addPlaylist(result.getPlaylist("My playlist!"));
//console.log(player);
    
var name = 'Rock and roll',
    playlist1 = result.getPlaylist(name),
    playlist2 = result.getPlaylist(name);
    
 console.log(playlist1);
 console.log(playlist2);
 
 console.log(playlist1.id === playlist2.id);

// var myPl = main.getPlayer("First");
// var myPlaylist1 = main.getPlaylist("Example Playlist 1");
// var myPlaylist2 = main.getPlaylist("Second Second");
// var myPlaylist3 = main.getPlaylist("Hello Hour");


// var playable1 = main.getAudio("La vien Rose", "Examplier", 3);
// myPlaylist1.addPlayable(playable1);

// myPl.addPlaylist(myPlaylist1);

// console.log(myPl);
// console.log(myPl.getPlaylistById(2));
//myPl.removePlaylist(myPlaylist1);
//console.log(myPl);
// myPl.addPlaylist(myPlaylist2);
// myPl.addPlaylist(myPlaylist3);
// console.log( myPl.listPlaylists(0, 3) );

// console.log("\n***********************\n");
// console.log(myPlaylist3.listPlayables(0, 1));

// myPl.removePlaylist(3);
// console.log( myPl.listPlaylists(0, 3) );

// console.log("--------------");
// console.log(myPl.contains(playable1, myPlaylist3));
