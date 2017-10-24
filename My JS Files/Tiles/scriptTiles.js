//18.8.2015 - A number of tiles with random colors are generated.
// When hovered over they should flip and turn black. On mouse leave, they should return to their normal color.
// !!!!! This script is designed and tested on Mozilla Firefox 40 !!!!!

// This module is used by the window.onload event down bellow.
var tiles = (function() {
	
	// It looks how big the window is and calculates how many rows and columns we will have.
	var width = window.innerWidth;
	var heigth = window.innerHeight;
	var xCells = Math.floor(width / 200);
	var yCells = Math.floor(heigth / 110);
	
	// Get the container div element and create a new fragment to hold the new cells.
	var container = document.getElementById("container");
	var fragment = document.createDocumentFragment();
	
	// List of colors.
	//List of colors: orange    blue,     green,    cyan,     yellow,     purple,   pink,      brown,      golden,   pool green,   gray,     yel/orang,   peach/red,   br/blue,   bl/green,  el/green
	var colors =   ["#fd5f00", "#397fdb", "green", "#4ec5ff", "#f6ba00", "#9344bb", "#e30472", "#990000", "#b2b758", "#00a372",   "#c0c0c0", "#ffa500",   "#fd482f",   "#0099cc", "#0d9a81", "#7be500"];
	
	// Helper function to generate a random number in the given min and max limits.
	function getRandomNumber(min, max) {
		return Math.floor(Math.random() * (max - min + 1) + min);
	}
	
	// Two nested for loops. Outer is for rows. Inner is for collumns.
	for (var i = 0; i < xCells; i += 1) {
		
		for (var j = 0; j < yCells; j += 1) {
			
			// We create a cell (new div), then pick a random color for it, 
			//then create a custom attribute to hold this color (we need it to restore the original color).
			// Lastly, we append the cell (every cell eventually) to the fragment. This is fast.
			var cell = document.createElement("div");
			var randomColor = colors[getRandomNumber(0, colors.length - 1)];
			cell.style.backgroundColor = randomColor;
			cell.setAttribute("previousColor", randomColor);
			
			fragment.appendChild(cell);
			
		} // inner for loop end
	} // outer for loop end
	
	// Here append the fragment to the container div. Now the cells are visible.
	container.appendChild(fragment);
	
	//First event listener. When the mouse gets over a cell, it is rotated and its background color is switched to black.
	container.addEventListener("mouseover", function(evnt) {
		var currentElement = evnt.target;
		
		currentElement.style.transform = "rotatex(180deg)"; 
    	currentElement.style.transitionDuration = "0.6s";
				
    	currentElement.style.backgroundColor = "black";		
	}, false);
	
	//Second event listener. When the mouse leaves the cell, the cell is rotated backwards and the background color is
	// restored by looking at the custom attribute we added to the cell.
	container.addEventListener("mouseout", function(evnt) {
		var currentElement = evnt.target;
		
		setTimeout(function(){
			currentElement.style.transform = "rotatex(-180deg)"; 
    		currentElement.style.transitionDuration = "0.6s";

    		currentElement.style.backgroundColor = currentElement.getAttribute("previousColor");
			
		}, 800);
		
		
		
	}, false);
});	
	
// When everything is loaded, execute the function above.	
window.onload = function(){
	tiles();	
};