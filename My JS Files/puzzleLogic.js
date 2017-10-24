var mainModule = (function() {

/**************************************************************************
*								Variable declarations
*
* 1. container - Selected the container div element. Used when appending the message when the puzzle is solved;
* 2. message - At the moment a new paragraph DOM element is created in the memory. Later text and style are added;
* 3. colors - array of strings (colors in hexadecimal format) /
* 		 a copy is created in giveValueToCell and four colors are extracted from it;  
* 4. values - array of ints / same as above, but the ints are used as the inner HTML of the cells of the table
* 5. fourCurrentValues - array to hold the randomly selected values from the values array;
* 6. smallest - the current smallest number we need to find and press its tile;
* 7. index - shows the index of the smallest number in fourCurrentValues;   
* 8. redShown - boolean flag to show if a red tile is up;
* 9. lastColor - has default value of "placeholder", saves the color of the tile that is currently red and will be
* 		used to restore its original color when the rigth tile is pressed;
* 10.previousTarget - saves the inner HTML of the current ev.target
* 11.previousTargetId -  used to select back the DOM element (the cell) we need return the color back to that it had originaly.
* 12.table - selected the DOM element table. Used to add an event to it as a parent and  when the puzzle is solved to remove the table.
* 13. cells - array of the selected by ID Dom Elements we will need for the puzzle.
/**************************************************************************/
	
	var container = document.getElementById("container");
	var message = document.createElement("p");
	
				    //orange   blue,     green,    cyan,     yellow,     purple,   pink,      brown,      golden
	var colors = ["#fd5f00", "#397fdb", "green", "#4ec5ff", "#f6ba00", "#9344bb", "#e30472", "#990000", "#b2b758"];
	var values = [1, 2, 3, 4, 5, 6, 7, 8, 9];
	var fourCurrentValues = [];
	var smallest = 0;
	var index = 0;
	var redShown = false;
	var lastColor = "placeholder";
	var previousTarget = 0;
	var previousTargetId = 0;
	var table = document.getElementsByTagName("table")[0];
	var cells = [
					document.getElementById("0"),
					document.getElementById("1"),
					document.getElementById("2"),
					document.getElementById("3")
				];	


/***************************************************************************
*								Helper functions.
/***************************************************************************/	

	/**
	 * Generates a random int in the given limits. Both inclusive.
	 * min - the lower limit
	 * max - the upper limit
	 */			
	function getRandomNumber(min, max) {
		return Math.floor(Math.random() * (max - min + 1) + min);
	}	
	
	/**
	 * Gives the cells random numeric values and colors.
	 * cells - array of selected DOM Elements (table cells)
	 * values - array of int values
	 * colors - array of strings (colors in hexadecimal)
	 */
	function giveValueToCell(cells, values, colors) {	
		var valuesCopy = values.slice();
		var colorsCopy = colors.slice();
		
		for (var i = 0; i < cells.length; i++) {
			
			var randomValueIndex = getRandomNumber(0, valuesCopy.length - 1);
			var theValue = valuesCopy[randomValueIndex];
			var theColor = colorsCopy[randomValueIndex];
			
			valuesCopy.splice(randomValueIndex, 1);
			colorsCopy.splice(randomValueIndex, 1);
			
			fourCurrentValues.push(theValue);
			cells[i].innerHTML = theValue;
			cells[i].style.backgroundColor = theColor;
			
		}
	} // end of giveValueToCell()
	
/***************************************************************************
*						  Making calls to the helper functions.
/***************************************************************************/	
		
	// generate values for cells, colors and adds the values to fourCurrentValues
	giveValueToCell(cells, values, colors);	
	//sort the array, so we know which one we should press next
	fourCurrentValues.sort(function(a, b){ 	return a - b; });
	
/***************************************************************************
* 							 Event Listener (main logic)
* 
* When a tile is pressed:
* 	The smallest number there is currently is taken from the fourCurrentValues by index
* 	If a wrong (larger) number is selected
* 		if already there is a red tile, select the previous target and return its original color
* 		save the current target's innerHTML, id and color in previousTarget, previousTargetId and lastColor
* 		color the current clicked tile red and raise the flag
* 	Else if the right tile is selected
* 		if there is a flag raised, color the previous target back to its original state
* 		color the current tile white and its innerHTML to black
* 		increment the index, so the next time we to have a new smallest number
* 		lower the flag for red tiles
* 	If all four tiles are colored white, delete table, create message and add it to the container.
/***************************************************************************/

	// event listenter for changing the color of the tiles on click
	table.addEventListener("click", function(ev) {
		smallest = fourCurrentValues[index];
		
		if (+ev.target.innerHTML > smallest) {
			
			if (redShown) {
				document.getElementById(previousTargetId.toString()).style.backgroundColor = lastColor; 
			}
			
			previousTarget = +ev.target.innerHTML;
			lastColor = ev.target.style.backgroundColor;
			previousTargetId = ev.target.id;
			
			ev.target.style.backgroundColor = "#dd0000"; //red
			redShown = true;
		}
		
		else if (+ev.target.innerHTML === smallest) {
			
			if (redShown) {
				document.getElementById(previousTargetId.toString()).style.backgroundColor = lastColor;
			}
			
			
			ev.target.style.backgroundColor = "white";
			ev.target.style.color = "black";
						
			 	
			index += 1;
			redShown = false;
			
			
			if (index === 4) {		
				
				// remove the table with the four cells we've used so far
				container.removeChild(table); 				
					
				// enter text and stylize the new message, then append it to the container div	
				message.innerHTML = "Alarm off!";	
				message.style.textAlign = "center";
				message.style.fontSize = "200%";
				message.style.backgroundColor = colors[getRandomNumber(0, colors.length - 1)];
				container.appendChild(message);
			}
		}// end of else if
				
	}, false);	
	
	
}());