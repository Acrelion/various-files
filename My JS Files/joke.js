// When I am sad, I stop being sad and be awesome instead.

var sad = {
    yes: true,
    stop: function() {
              this.yes = false;
    }
};

var beAwesome = function() {
    console.log("I am awesome!");
};

if ( sad ) {
    sad.stop();
    beAwesome();
}